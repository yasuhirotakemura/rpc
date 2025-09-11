from dataclasses import dataclass
from typing import Any

from src.domain.exceptions.rpc_error import RpcError
from src.domain.exceptions.rpc_type_casting_error import RpcTypeCastingError
from src.domain.exceptions.rpc_unknown_type_error import RpcUnknownTypeError

@dataclass
class RpcRequest:
    method: str
    params: list[str]
    param_types: list[str]
    id: int

    def casted_params(self) -> list[Any]:
        TYPE_MAP = {
            "int": int,
            "float": float,
            "str": str,
            "bool": lambda x: x.lower() in ("true", "1", "yes"),
        }

        casted = []
        for p, t in zip(self.params, self.param_types):
            try:
                if t not in TYPE_MAP:
                    raise RpcUnknownTypeError(f"Unknown parameter type: {t}")
                casted.append(TYPE_MAP[t](p))
            except RpcError as e:
                raise RpcTypeCastingError(
                    f"Failed to cast param '{p}' to type '{t}'"
                ) from e

        return casted