import math

class RpcFunctions:
    def floor(self, x: float) -> int:
        return math.floor(x)

    def n_root(self, x: int, y: int) -> float:
        if y <= 0:
            raise ValueError("n must be positive")

        # 負数対応: n が奇数なら負の値もOK
        if x < 0 and y % 2 == 1:
            return -((-x) ** (1.0 / y))

        return x ** (1.0 / y)

    def reverse(self, x: str) -> str:
        return ''.join(list(reversed(x)))

    def valid_anagram(self, str1: str, str2: str) -> str:
        return sorted(str1) == sorted(str2)

    def sort(self, str_arr: list[str]) -> list[str]:
        return sorted(str_arr)