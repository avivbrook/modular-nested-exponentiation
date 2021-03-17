from typing import Tuple

def ext_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Given nonnegative integers a and b, uses the extended Euclidean algorithm to
    compute gcd(a,b) and the coefficients of Bézout's identity -- integers x and
    y such that
        ax + by = gcd(a,b).
    
    Parameters
    ----------
    a, b: nonnegative integers.

    Returns
    -------
        gcd(a,b), x, y.
    """
    if a < 0 or b < 0:
        raise ValueError('a and b must be nonnegative integers')
    
    prev_r, r, prev_x, x = a, b, 1, 0
    while r: # while remainder > 0
        q = prev_r // r # quotient
        prev_r, prev_x, r, x = r, x, prev_r-q*r, prev_x-q*x
    return prev_r, prev_x, ((prev_r - prev_x*a)//b if b else 0)