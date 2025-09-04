import socket
from src.domain.interfaces.socket_handler import SocketHandler

class UnixSocketHandler(SocketHandler):
    def __init__(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    def bind(self, address: str) -> None:
        self.sock.bind(address)

    def recvfrom(self, bufsize: int):
        return self.sock.recvfrom(bufsize)

    def sendto(self, data: bytes, address: str):
        self.sock.sendto(data, address)

    def close(self):
        self.sock.close()
