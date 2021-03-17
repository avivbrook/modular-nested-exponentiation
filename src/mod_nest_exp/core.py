from typing import List
from sympy.ntheory import totient
from .utils import pow_lt, pow_list

try:
    from gmpy2 import gcd, powmod, gcdext
except ImportError:
    from math import gcd
    powmod = pow
    from .gcd import ext_gcd as gcdext

def mod_nest_exp(seq: List[int], m: int) -> int:
    """
    Given an arbitrarily long sequence of positive integers
    seq = [a₁, a₂, a₃, ..., aₙ] and a positive integer m, computes
    a₁^(a₂^(a₃^(···^aₙ))) mod m.
    Parameters
    ----------
    seq: list of positive integers.
    m: positive integer
        The modulus of congruence.
    
    Returns
    -------
        seq[0]^(seq[1]^(seq[2]^···)) mod m.
    """
    if m < 1:
        raise ValueError('m must be a positive integer')
    for a in seq:
        if a < 1:
            raise ValueError('seq may only contain positive integers')

    if m == 1: # 1 divides every integer
        return 0
    l = len(seq)
    if not l: # if len(seq) == 0
        return 1%m
    elif l == 1: # if len(seq) == 1
        return seq[0]%m

    def _mod_nest_exp(seq, m):
        if m == 1: # 1 divides every integer
            return 0
        if len(seq) == 2: # recursive base case
            return powmod(seq[0], seq[1], m)
        
        b, e = seq[0], seq[1:] # base and exponent
        g = gcd(b, m)
        if g == 1:
            return powmod(b, _mod_nest_exp(e, totient(m)), m)
        
        n, k = m//g, 1
        g_ = gcd(g, n)
        while g_ > 1:
            n //= g_
            k += 1
            g_ = gcd(g, n)
        h = m//n
        _, x, y = gcdext(n, h)
        return (h*(y%n)*powmod(b, _mod_nest_exp(e, totient(n)), n)+
                n*(x%h)*(powmod(b, pow_list(e), h) if pow_lt(e, k) else 0))%m
    
    return _mod_nest_exp(seq, m)