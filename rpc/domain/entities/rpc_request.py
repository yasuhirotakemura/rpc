from dataclasses import dataclass
from typing import Any

@dataclass
class RpcRequest:
    method: str
    params: list[Any]
    id: int