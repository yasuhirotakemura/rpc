from dataclasses import asdict
import logging
import os

from rpc.domain.interfaces.serializer import Serializer
from rpc.domain.entities.rpc_request import RpcRequest
from rpc.domain.interfaces.socket_handler import SocketHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RpcClient:
    def __init__(self, server_address: str, client_address: str, serializer: Serializer, socket_handler: SocketHandler) -> None:
        self.server_address: str = server_address
        self.client_address: str = client_address
        self.socket_handler = socket_handler
        self.serializer = serializer

    def remove_file_if_exists(self) -> None:
        """同じクライアントアドレスのファイルがある場合に削除する"""
        try:
            os.unlink(self.client_address)
        except FileNotFoundError:
            pass

    def display_receive_data(self, received_data : bytes, server_address) -> None:
        """ターミナルに受信データを表示する"""
        data_str: str = self.serializer.decode(received_data)
        logger.info("A message of %d bytes was sent from server address %s",
                    len(received_data), server_address)
        logger.debug("Server response: %s", data_str)

    def receive_data(self) -> None:
        """サーバーからのデータを受信する"""
        logger.info("Waiting for a message from the server...")
        data, server_address = self.socket_handler.recvfrom(4096)
        self.display_receive_data(data, server_address)

    def sent_data(self) -> None:
        """サーバーにデータを送信する"""
        while True:
            method_name: str = input("Enter the method name : ")
            params: str = input("Enter the parameters (comma-separated) : ")

            rpc_request: RpcRequest = RpcRequest(
                method=method_name,
                params=[param.strip() for param in params.split(',')],
                id=1
            )

            request_data = self.serializer.encode(asdict(rpc_request))

            try:
                self.socket_handler.sendto(request_data, self.server_address)
                logger.info("The following data was sent to the server: %s", request_data)
            except Exception as e:
                logger.error("Error while sending data: %s", e)

    def start_client(self) -> None:
        """クライアントを起動する"""
        self.remove_file_if_exists()

        self.socket_handler.bind(self.client_address)

        logger.info('A socket was started with client address "%s"', self.client_address)

        self.sent_data()