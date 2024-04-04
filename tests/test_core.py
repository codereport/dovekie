import operator as op
from itertools import accumulate

from dovekie.core import _add, _b, _fst, _l_, _phi1_, _r_, _snd


def test_l():
    assert _l_(1, None) == 1

def test_r():
    assert _r_(None, 2) == 2

def mco(xs: list[int]) -> int:
    return max(accumulate(xs, _phi1_(op.add, op.mul, _r_)))

def test_phi1_mco():
    assert mco([1, 0, 1, 1, 1, 0, 0, 1, 1, 0]) == 3

def test_b():
    assert _b(op.neg, _add(1))(1) == -2

def test_fst():
    x = [1, 2, 4]
    assert list(map(_snd, enumerate(x))) == x

def test_snd():
    x = [1, 2, 4]
    assert list(map(_fst, enumerate(x))) == [0, 1, 2]
