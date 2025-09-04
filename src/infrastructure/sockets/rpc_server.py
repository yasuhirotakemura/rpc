from dataclasses import asdict
import json
import logging

from src.application.config import METHOD_TABLE
from src.domain.interfaces.serializer import Serializer
from src.domain.entities.rpc_request import RpcRequest
from src.domain.entities.rpc_response import RpcResponse
from src.domain.interfaces.socket_handler import SocketHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RpcServer:
    def __init__(self, server_address: str, serializer: Serializer, socket_handler: SocketHandler):
        self.server_address: str = server_address
        self.socket_handler: SocketHandler = socket_handler
        self.serializer: Serializer = serializer

    def sent_data(self, client_address: str, response: RpcResponse) -> None:
        """クライアントにデータを送信"""
        response_data = self.serializer.encode(asdict(response))

        try:
            self.socket_handler.sendto(response_data, client_address)
            logger.info("The following data was sent to the client: %s", response_data)
        except Exception as e:
            logger.error("Error while sending data: %s", e)

    def display_receive_data(self, received_data: bytes, client_address: str) -> None:
        """受信データをログに出力"""
        data_str = self.serializer.decode(received_data)

        logger.info("A message of %d bytes was sent from client address %s",
                    len(received_data), client_address)
        logger.debug("Client data: %s", data_str)

    def process_request(self, request: RpcRequest) -> RpcResponse:
        """リクエストを処理してレスポンスを生成"""
        try:
            if request.method not in METHOD_TABLE:
                raise ValueError("Unknown method: %s" % request.method)

            method_func = METHOD_TABLE[request.method]
            result = method_func(*request.params)

            return RpcResponse(
                results=str(result),
                result_type=type(result).__name__,
                id=request.id
            )
        except Exception as e:
            return RpcResponse(error=str(e), id=request.id)

    def receive_data(self) -> None:
        """クライアントからのデータを受信して処理"""

        while True:
            logger.info("Waiting for message...")

            try:
                received_data, client_address = self.socket_handler.recvfrom(4096)
                self.display_receive_data(received_data, client_address)

                request_dict = self.serializer.decode(received_data)
                request = RpcRequest(**request_dict)

                logger.info("Received from %s: %s", client_address, request)
                response = self.process_request(request)
                self.sent_data(client_address, response)

            except json.JSONDecodeError as e:
                logger.error("Invalid JSON received: %s", e)
                error_response = RpcResponse(error=f"Invalid JSON: {str(e)}")
                self.sent_data(client_address, error_response)

            except Exception as e:
                logger.error("Unexpected server error: %s", e)
                error_response = RpcResponse(error=f"Server error: {str(e)}")
                self.sent_data(client_address, error_response)

    def start(self) -> None:
        """サーバーを起動"""
        try:
            self.socket_handler.bind(self.server_address)
            logger.info("Server started on: %s", self.server_address)
            self.receive_data()
        except Exception as e:
            logger.error("Server start failed: %s", e)
        finally:
            self.socket_handler.close()