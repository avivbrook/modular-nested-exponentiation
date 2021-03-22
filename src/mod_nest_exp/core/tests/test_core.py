from typing import Tuple
from statistics import mean, median, stdev
from mod_nest_exp import mod_nest_exp
from mod_nest_exp.testing import benchmark, rand_n_digit_int, dot_to_and

def test_core(
    list_lengths: Tuple[int],
    bit_lengths: Tuple[int],
    mod_bit_lengths: Tuple[int],
    num_iters: int = 1000,
    max_seconds: int = None,
    latex: bool = False
):
    if latex:
        print('\\begin{tabular}{cc|%s}' % ('r@{.}l'*len(list_lengths)*2))
        print('\t\\toprule')
        print('\t& \\multicolumn{1}{c}{} & \\multicolumn{%d}{c}{sequence length $\\ell$} \\\\' % (len(list_lengths)*4))
        print('\t& \\multicolumn{1}{c}{} & %s \\\\' % ' & '.join(['\\multicolumn{4}{c}{$%d$}' % l for l in list_lengths]))
        print('\t%s' % ' '.join(['\\cmidrule(r){%d-%d}' % (4*i+3,4*i+6) for i in range(len(list_lengths))]))
        print('\t$B$ & \\multicolumn{1}{c}{$b$} & %s \\\\' % ' & '.join(['\\multicolumn{2}{c}{mean} & \\multicolumn{2}{c}{stdev}' for _ in list_lengths]))
    else:
        print('Running %s on sequences of l pseudorandom b-bit positive integers over a B-bit modulus (%d runs' % (mod_nest_exp.__name__, num_iters), end='')
        if max_seconds is not None:
            print(' / %ds timeout' % max_seconds, end='')
        print(' per table entry)')
        Bp = len(str(max(mod_bit_lengths, key=lambda B: len(str(B))))) + 1
        bp = len(str(max(bit_lengths, key=lambda b: len(str(b))))) + 1
        lp = len('1000.00') + 1
        print('='*(2*len(list_lengths)*(lp+1)+Bp+bp+3))
        print(' '*(Bp+bp+1), 'sequence length l'.center(2*len(list_lengths)*(lp+1)))
        print(' '*(Bp+bp+1), ' '.join([str(l).center(2*(lp+1)-1) for l in list_lengths]))
        print(' '*(Bp+bp+1), ' '.join(['-'*(2*(lp+1)-1) for _ in list_lengths]))
        print('B'.rjust(Bp), 'b'.rjust(bp), ' '.join([s.rjust(lp) for s in ['mean', 'stdev']*len(list_lengths)]))
    
    for Bm in mod_bit_lengths:
        if latex:
            print('\t\\midrule')
            print('\t\\multirow{%d}{*}{$%d$}' % (len(bit_lengths), Bm))
        else:
            print('-'*(2*len(list_lengths)*(lp+1)+Bp+bp+3))
        for b, Ba in enumerate(bit_lengths):
            if latex:
                print('\t\t& $%d$ ' % Ba, end='')
            else:
                if b == len(bit_lengths)//2:
                    print(str(Bm).center(Bp), end=' ')
                else:
                    print(' '*Bp, end=' ')
                print(str(Ba).rjust(bp), end=' |')
            for l in list_lengths:
                args = (([rand_n_digit_int(Ba) for _ in range(l)], rand_n_digit_int(Bm)) for _ in range(num_iters))
                times = benchmark((mod_nest_exp,), args, max_seconds=max_seconds)[mod_nest_exp]
                if latex:
                    print('& %s & %s' % (dot_to_and('%.2f'%(mean(times)*1000)), dot_to_and('%.2f'%(stdev(times)*1000))), end='')
                else:
                    m = ('%.2f'%(mean(times)*1000)).split('.')
                    s = ('%.2f'%(stdev(times)*1000)).split('.')
                    print(m[0].rjust(lp-4), '.', m[1].ljust(3), sep='', end=' ')
                    print(s[0].rjust(lp-4), '.', s[1].ljust(3), sep='', end=' ')
            if latex:
                print(' \\\\')
            else:
                print()
    
    if latex:
        print('\t\\bottomrule')
        print('\\end{tabular}')
    else:
        print('='*(2*len(list_lengths)*(lp+1)+Bp+bp+3))