from random import randrange
from typing import Dict
from collections import Counter
from .small_primes import small_primes

try:
    from sympy.ntheory import isprime
except (ImportError, ModuleNotFoundError):
    from .primes import isprime

try:
    from gmpy2 import gcd, powmod
except ImportError:
    from math import gcd
    powmod = pow

def pollard_brent(n: int) -> int:
    """
    Given a positive integer n, returns a nontrivial factor of n if n is
    composite; if n is prime, returns n. Uses Pollard's rho algorithm with
    Brent's cycle finding method:
    https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/.

    Parameters
    ----------
    n: positive integer.

    Returns
    -------
        a nontrivial factor of n if n is composite; n otherwise.
    """
    if not n&1: # if n%2 == 0
        return 2
    elif not n%3: # if n%3 == 0
        return 3
    
    y, c, m = randrange(1, n), randrange(1, n), randrange(1, n)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range(r):
            y = (powmod(y, 2, n) + c) % n
        k = 0
        while k < r and g == 1:
            ys = y
            for i in range(min(m, r-k)):
                y = (powmod(y, 2, n) + c) % n
                q = q*abs(x-y) % n
            g = gcd(q, n)
            k += m
        r *= 2
    if g == n:
        while True:
            ys = (powmod(ys, 2, n) + c) % n
            g = gcd(abs(x-ys), n)
            if g > 1:
                break
    return g

def large_factors(n: int) -> Dict[int, int]:
    """
    Given a positive integer n, returns a dict containing the prime factors of n
    as keys and their respective multiplicities as values.

    Parameters
    ----------
    n: positive integer.

    Returns
    -------
        a dict containing the prime factors of n as keys and their respective
        multiplicities as values.
    """
    factors = Counter()
    while n > 1:
        if isprime(n):
            factors[n] += 1
            break
        factor = pollard_brent(n)
        factors += large_factors(factor)
        n //= factor
    return factors

def factorint(n: int) -> Dict[int, int]:
    """
    Given a positive integer n, returns a dict containing the prime factors of n
    as keys and their respective multiplicities as values.

    Parameters
    ----------
    n: positive integer.

    Returns
    -------
        a dict containing the prime factors of n as keys and their respective
        multiplicities as values.
    """
    factors = Counter()
    for p in small_primes:
        while not n%p: # while n%p == 0
            factors[p] += 1
            n //= p
    if n == 1:
        return factors
    return factors + large_factors(n)