from enum import Enum, auto

class ErrorType(Enum):
    INFO = auto()
    WARNING = auto()
    ERROR = auto()

class RpcError(Exception):
    """RPC全般の例外基底クラス"""
    def __init__(self, message: str, error_type: ErrorType):
        super().__init__(message)
        self.error_type = error_type