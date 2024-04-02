import operator as op
from itertools import accumulate

from dovekie.core import _l_, _r_, _phi1_

def test_l():
    assert _l_(1, None) == 1

def test_r():
    assert _r_(None, 2) == 2

def mco(xs: list[int]) -> int:
    return max(accumulate(xs, _phi1_(op.add, op.mul, _r_)))

def test_phi1_mco():
    assert mco([1, 0, 1, 1, 1, 0, 0, 1, 1, 0]) == 3
