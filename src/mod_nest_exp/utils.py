from typing import List
from decimal import Decimal
from math import ceil

def pow_lt(seq: List[int], k: Decimal) -> bool:
    """
    Given an arbitrarily long sequence of positive integers
    seq = [e₁, e₂, e₃, ..., eₙ] and a positive number k, returns True if and only if
    e₁^(e₂^(e₃^(···^eₙ))) < k.
    Inputs are not validated. That is, k is assumed to be positive and the
    elements of seq are assumed to be positive integers.
    Parameters
    ----------
    seq: list of positive integers.
    k: positive number.
    Returns
    -------
        True if and only if seq[0]^(seq[1]^(seq[2]^···)) < k.
    """
    if not len(seq): # if len(seq) == 0
        return 1 < k

    def _pow_lt(seq, k):
        if len(seq) == 1 or seq[0] == 1:
            return seq[0] < k
        if seq[1]*(seq[0].bit_length()-1) >= ceil(k).bit_length():
            return False
        l = Decimal(k).ln()/Decimal(seq[0]).ln() # high precision logarithm
        return _pow_lt(seq[1:], l) if l > 1 else False

    return _pow_lt(seq, k)

def pow_list(seq: List[Decimal]) -> Decimal:
    """
    Given an arbitrarily long sequence of numbers seq = [e₁, e₂, e₃, ..., eₙ],
    computes e₁^(e₂^(e₃^(···^eₙ))).
    The elements of seq are assumed to be numbers without validation.
    Parameters
    ----------
    seq: list of numbers.
    Returns
    -------
        seq[0]^(seq[1]^(seq[2]^···)).
    """
    l = len(seq)
    if not l: # if len(seq) == 0
        return 1
    elif l == 1: # if len(seq) == 1
        return seq[0]

    def _pow_list(seq):
        if seq[0] == 1:
            return 1
        if len(seq) == 2:
            return seq[0]**seq[1]
        return seq[0]**_pow_list(seq[1:])
    
    return _pow_list(seq)