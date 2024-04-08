import operator as op
from itertools import accumulate

import dovekie.core as d


def test_l():
    assert d.l(1, None) == 1

def test_r():
    assert d.r(None, 2) == 2

def mco(xs: list[int]) -> int:
    return max(accumulate(xs, d.phi1(op.add, op.mul, d.r)))

def test_phi1_mco():
    assert mco([1, 0, 1, 1, 1, 0, 0, 1, 1, 0]) == 3

def test_b():
    assert d.b(op.neg, d.addl(1))(1) == -2

def test_fst():
    x = [1, 2, 4]
    assert list(map(d.snd, enumerate(x))) == x

def test_snd():
    x = [1, 2, 4]
    assert list(map(d.fst, enumerate(x))) == [0, 1, 2]
