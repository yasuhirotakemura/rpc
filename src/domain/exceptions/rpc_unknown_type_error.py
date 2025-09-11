from src.domain.exceptions.rpc_error import ErrorType, RpcError

class RpcUnknownTypeError(RpcError):
    """未知の型が指定された場合の例外"""
    def __init__(self, message: str):
        super().__init__(message, ErrorType.WARNING)