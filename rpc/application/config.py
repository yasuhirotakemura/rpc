# config.py
from rpc.domain.services.rpc_functions import RpcFunctions


METHOD_TABLE = {
    "floor": RpcFunctions.floor,
    "nroot": RpcFunctions.n_root,
    "reverse": RpcFunctions.reverse,
    "validAnagram": RpcFunctions.valid_anagram,
    "sort": RpcFunctions.sort
}