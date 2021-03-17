from random import randint
from statistics import mean, median, stdev
from mod_nest_exp import mod_nest_exp
from mod_nest_exp.testing import benchmark

def rand_n_digit_int(num_digits: int, base: int = 2):
    return randint(base**(num_digits-1), base**num_digits-1)

def dot_to_and(s: str, bold: bool = False) -> str:
    if bold:
        t = s.split('.')
        return '\\textbf{%s}&\\textbf{%s}'%(t[0],t[1]) if '.' in s else '\\textbf{%s}&'%s
    else:
        return s.replace('.','&') if '.' in s else s+'&'

def test_core(
    list_lengths: tuple[int],
    bit_lengths: tuple[int],
    mod_bit_length: int,
    num_iters: int = 1000,
    max_seconds: int = None,
    latex: bool = False
):
    if latex:
        print('\t\\toprule')
        print('\t\\multicolumn{2}{c}{} & \\multicolumn{%i}{c}{max bit length $b$} \\tabularnewline'%(2*len(bit_lengths)))
        print('\t\\multicolumn{2}{c}{} ', *(['\\multicolumn{2}{c}{\\textbf{%i}} '%b for b in bit_lengths]), sep='& ', end=' & \\multicolumn{2}{c}{\\textbf{mean}} \\tabularnewline\n\t\\midrule\n')
    else:
        print('='*50)
        print('Benchmarking %s (%i-bit moduli)' % (mod_nest_exp.__name__, mod_bit_length))
        print('='*50)
    
    for i, list_len in enumerate(list_lengths):
        if latex:
            if i:
                print('\t', end='')
            else:
                print('\t\\multirow{%i}{*}{\\shortstack{sequence\\\\length\\\\$\\ell$}}'%len(list_lengths), end=' ')
            print('& \\multicolumn{1}{c|}{\\textbf{%i}}'%list_len, end='', flush=True)
        else:
            print('lists of length %i:' % list_len)
        for bit_len in bit_lengths:
            if not latex:
                print('\tbit length %i' % bit_len)
            args = (([rand_n_digit_int(bit_len) for _ in range(list_len)], rand_n_digit_int(mod_bit_length)) for _ in range(num_iters))
            times = benchmark((mod_nest_exp,), args, max_seconds=max_seconds)[mod_nest_exp]
            if not latex:
                print('\tstats from %i runs' % len(times))
            stats = (
                ('mean', mean(times)),
                ('median', median(times)),
                ('stdev', stdev(times))
            )
            if latex:
                print(' & %s'%dot_to_and('%.2f' % mean(times)), end='', flush=True)
            else:
                for name, value in stats:
                    print('\t\t%s: %.2f ms' % (name, value*1000))
        

# latex functionality does not work as of now
if __name__ == '__main__':
    bit_lengths = (16, 128, 1024)
    list_lengths = (10, 100, 1000)
    latex = False

    if latex:
        print('\\begin{tabular}{ll|',*(['r@{.}l']*len(bit_lengths)), sep='', end='|r@{.}l}\n')

    for mod_bit_length in (16, 32, 64):
        test_core(
            list_lengths=list_lengths,
            bit_lengths=bit_lengths,
            mod_bit_length=mod_bit_length,
            max_seconds=30,
            latex=latex
        )