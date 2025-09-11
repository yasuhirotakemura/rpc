from src.infrastructure.serializers.json_serializer import JsonSerializer


def test_encode_decode_roundtrip():
    serializer = JsonSerializer()
    data = {"foo": "bar", "num": 123}
    encoded = serializer.encode(data)
    assert isinstance(encoded, bytes)
    decoded = serializer.decode(encoded)
    assert decoded == data
