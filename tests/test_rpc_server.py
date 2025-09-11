from src.infrastructure.sockets.rpc_server import RpcServer
from src.domain.entities.rpc_request import RpcRequest


def create_server():
    # Serializer and socket handler are not used in process_request
    return RpcServer("/tmp/server", None, None)


def test_process_request_floor():
    server = create_server()
    request = RpcRequest(method="floor", params=[3.7], id=1)
    response = server.process_request(request)
    assert response.results == "3"
    assert response.result_type == "int"
    assert response.error is None
    assert response.id == 1


def test_process_request_unknown_method():
    server = create_server()
    request = RpcRequest(method="foo", params=[], id=2)
    response = server.process_request(request)
    assert response.results is None
    assert response.error.startswith("Unknown method")
    assert response.id == 2


def test_process_request_method_error():
    server = create_server()
    request = RpcRequest(method="nroot", params=[16, 0], id=3)
    response = server.process_request(request)
    assert response.results is None
    assert "n must be positive" in response.error
    assert response.id == 3
