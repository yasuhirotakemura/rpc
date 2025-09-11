# config.py
from src.domain.services.rpc_functions import RpcFunctions

# Instantiate RpcFunctions so that bound methods can be used in the table
rpc_functions = RpcFunctions()

METHOD_TABLE = {
    "floor": rpc_functions.floor,
    "nroot": rpc_functions.n_root,
    "reverse": rpc_functions.reverse,
    "validAnagram": rpc_functions.valid_anagram,
    "sort": rpc_functions.sort,
}
