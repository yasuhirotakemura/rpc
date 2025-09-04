from src.infrastructure.serializers.json_serializer import JsonSerializer
from src.infrastructure.sockets.rpc_client import RpcClient
from src.infrastructure.sockets.unix_socket_handler import UnixSocketHandler

def main():
    server_address: str = '127.0.0.1'
    client_address: str = '127.0.0.2'

    client: RpcClient = RpcClient(server_address, client_address, JsonSerializer(), UnixSocketHandler())

    client.start_client()

if __name__ == "__main__":
    main()