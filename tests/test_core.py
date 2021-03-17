from random import randint
from statistics import mean, median, stdev
from mod_nest_exp import mod_nest_exp
from mod_nest_exp.testing import benchmark

def rand_n_digit_int(num_digits: int, base: int = 2):
    return randint(base**(num_digits-1), base**num_digits-1)

def test_core(
    list_lengths: tuple[int],
    bit_lengths: tuple[int],
    mod_bit_length: int,
    num_iters: int = 1000,
    max_seconds_per_trial: int = None
):
    print('='*80)
    print('Benchmarking %s (%i-bit moduli)' % (mod_nest_exp.__name__, mod_bit_length))
    print('='*80)
    
    for bit_len in bit_lengths:
        print('%i bit numbers:' % bit_len)
        for list_len in list_lengths:
            print('\tlists of length %i' % list_len)
            args = (([rand_n_digit_int(bit_len) for _ in range(list_len)], rand_n_digit_int(mod_bit_length)) for _ in range(num_iters))
            times = benchmark((mod_nest_exp,), args, max_seconds=max_seconds_per_trial)[mod_nest_exp]
            print('\tstats from %i runs' % len(times))
            stats = (
                ('mean', mean(times)),
                ('median', median(times)),
                ('stdev', stdev(times))
            )
            for name, value in stats:
                print('\t\t%s: %.2e seconds' % (name, value))

if __name__ == '__main__':
    test_core(
        list_lengths=(10, 100, 1000),
        bit_lengths=(10, 100, 1000),
        mod_bit_length=64
    )