import operator as op
from itertools import accumulate

import dovekie.core as dk


def test_l():
    assert dk.l(1, None) == 1

def test_r():
    assert dk.r(None, 2) == 2

def mco(xs: list[int]) -> int:
    return max(accumulate(xs, dk.phi1(op.add, op.mul, dk.r)))

def test_phi1_mco():
    assert mco([1, 0, 1, 1, 1, 0, 0, 1, 1, 0]) == 3

def test_b():
    assert dk.b(op.neg, dk.addl(1))(1) == -2

def test_fst():
    x = [1, 2, 4]
    assert list(map(dk.snd, enumerate(x))) == x

def test_snd():
    x = [1, 2, 4]
    assert list(map(dk.fst, enumerate(x))) == [0, 1, 2]

def sos(s: str) -> int:
    return sum(map(dk.b1(abs, dk.psi(op.sub, ord)), s[1:], s))

def test_b1_psi_sos():
    assert sos("hello") == 13
