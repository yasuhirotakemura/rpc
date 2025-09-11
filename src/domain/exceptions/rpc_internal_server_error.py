from src.domain.exceptions.rpc_error import ErrorType, RpcError

class RpcInternalServerError(RpcError):
    def __init__(self, message: str):
        super().__init__(message, ErrorType.ERROR)