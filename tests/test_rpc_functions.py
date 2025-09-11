import pytest
from src.domain.services.rpc_functions import RpcFunctions

rpc = RpcFunctions()

def test_floor():
    assert rpc.floor(3.7) == 3
    assert rpc.floor(-3.7) == -4

def test_n_root_positive():
    assert rpc.n_root(27, 3) == pytest.approx(3.0)


def test_n_root_negative_odd():
    assert rpc.n_root(-27, 3) == pytest.approx(-3.0)


def test_n_root_invalid_n():
    with pytest.raises(ValueError):
        rpc.n_root(16, 0)


def test_reverse():
    assert rpc.reverse("abcdef") == "fedcba"


def test_valid_anagram_true():
    assert rpc.valid_anagram("anagram", "nagaram") is True


def test_valid_anagram_false():
    assert rpc.valid_anagram("rat", "car") is False


def test_sort_strings():
    assert rpc.sort(["banana", "apple", "cherry"]) == ["apple", "banana", "cherry"]
