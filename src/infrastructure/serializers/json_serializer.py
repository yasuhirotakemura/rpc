import json
from src.domain.interfaces.serializer import Serializer

class JsonSerializer(Serializer):
    def encode(self, data: dict) -> bytes:
        return json.dumps(data).encode('utf-8')
    
    def decode(self, data: bytes) -> dict:
        return json.loads(data.decode('utf-8'))