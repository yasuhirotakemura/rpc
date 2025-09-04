from abc import ABC, abstractmethod

class Serializer(ABC):
    @abstractmethod
    def encode(self, data: dict) -> bytes:
        pass

    @abstractmethod
    def decode(self, data: bytes) -> dict:
        pass