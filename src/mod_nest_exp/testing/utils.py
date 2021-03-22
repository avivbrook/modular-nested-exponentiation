from random import randint
from typing import Iterable
from itertools import groupby

def rand_n_digit_int(num_digits: int, base: int = 2):
    return randint(base**(num_digits-1), base**num_digits-1)

def all_equal(seq: Iterable):
    g = groupby(seq)
    return next(g, True) and not next(g, False)

def dot_to_and(s: str, bold: bool = False) -> str:
    if bold:
        t = s.split('.')
        return '\\textbf{%s}&\\textbf{%s}'%(t[0],t[1]) if '.' in s else '\\textbf{%s}&'%s
    else:
        return s.replace('.','&') if '.' in s else s+'&'