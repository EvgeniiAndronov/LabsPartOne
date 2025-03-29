import pytest
from num_6 import b2int

def test_b2int():
    assert b2int("1") == 1
    assert b2int("0") == 0
    assert b2int("101") == 5
    assert b2int("111") == 7