from dataclasses import dataclass
from typing import Optional

@dataclass
class RpcResponse:
    results: Optional[str] = None
    result_type: Optional[str] = None
    error: Optional[str] = None
    id: Optional[int] = None