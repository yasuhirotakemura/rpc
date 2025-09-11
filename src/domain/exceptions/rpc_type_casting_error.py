from src.domain.exceptions.rpc_error import ErrorType, RpcError

class RpcTypeCastingError(RpcError):
    """パラメータの型変換に失敗した場合の例外"""
    def __init__(self, message: str):
        super().__init__(message, ErrorType.WARNING)