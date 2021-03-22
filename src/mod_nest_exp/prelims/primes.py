from random import randrange
from .small_primes import small_primes, max_prime

try:
    from gmpy2 import powmod
except ImportError:
    powmod = pow

def isprime(n: int, k: int = 3) -> bool:
    """
    Given an integer n and a positive integer k, determines if n is likely to be
    prime using the Miller-Rabin primality test. The probability of a false
    positive is 1/4ᵏ.

    Parameters
    ----------
    n: integer.
    k: positive integer, optional (default is 3)
        The number of rounds of testing to perform.
    
    Returns
    -------
        True if n is likely to be prime; False otherwise.
    """
    if n < 2:
        return False
    elif n < 4:
        return n > 1 # 2 and 3 are trivial primes
    elif not n&1: # if n%2 == 0
        return False
    elif n < max_prime:
        return n in small_primes
    
    d, r = n-1, 0 # n = 2ʳ·d + 1
    while not d&1: # while d%2 == 0
        d >>= 1
        r += 1
    
    for _ in range(k):
        x = powmod(randrange(2, n-1), d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(r-1):
            x = powmod(x, 2, n)
            if x == 1:
                return False
            elif x == n-1:
                break
        else:
            return False
    return True