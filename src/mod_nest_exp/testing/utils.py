from typing import Iterable
from itertools import groupby

def all_equal(seq: Iterable):
    g = groupby(seq)
    return next(g, True) and not next(g, False)