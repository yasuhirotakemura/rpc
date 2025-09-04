from src.infrastructure.serializers.json_serializer import JsonSerializer
from src.infrastructure.sockets.rpc_server import RpcServer
from src.infrastructure.sockets.unix_socket_handler import UnixSocketHandler

def main():
    server_address = '127.0.0.1'

    server = RpcServer(server_address, JsonSerializer(), UnixSocketHandler())

    server.start()

if __name__ == "__main__":
    main()