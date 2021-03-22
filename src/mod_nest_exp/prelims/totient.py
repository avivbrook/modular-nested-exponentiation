from .factor import factorint

def totient(n: int) -> int:
    """
    Given a positive integer n, returns φ(n), which is the number of positive
    integers ≤ n that are coprime to n. Uses the product formula for φ: letting
        n = p₁ᵉ¹p₂ᵉ²···pᵣᵉʳ
    be the unique prime factorisation of n, where r is a nonnegative integer,
    p₁ < p₂ < ··· < pᵣ are distinct primes, and each eᵢ is a positive integer,
        φ(n) = n·(1 - 1/p₁)·(1 - 1/p₂)···(1 - 1/pᵣ).

    Parameters
    ----------
    n: positive integer.

    Returns
    -------
        φ(n).
    """
    for p in factorint(n).keys():
        n -= n//p
    return n