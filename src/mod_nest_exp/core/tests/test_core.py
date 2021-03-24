import pytest
import signal
from time import time
from random import randrange, randint
from mod_nest_exp import mod_nest_exp
from mod_nest_exp.core.utils import pow_list

try:
    from gmpy2 import powmod
except ImportError:
    powmod = pow

def pytest_generate_tests(metafunc):
    funcarglist = metafunc.cls.params[metafunc.function.__name__]
    argnames = sorted(funcarglist[0])
    metafunc.parametrize(
        argnames, [[funcargs[name] for name in argnames] for funcargs in funcarglist]
    )

def handler(signum, frame):
    raise RuntimeError('Timed out')

class Timeout:
    def __init__(self, seconds=1, error_message='Timed out'):
        self.seconds = seconds
        self.error_message = error_message
    
    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)
    
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    
    def __exit__(self, type, value, traceback):
        signal.alarm(0)

class TestCore:
    params = {
        'test_core': [dict(seq=[randrange(1, 5) for _ in range(randint(1, 5))], m=randrange(1, 2**64)) for _ in range(100)]
    }

    def test_core(self, seq, m):
        try:
            with Timeout():
                r1 = powmod(seq[0], pow_list(seq[1:]), m)
        except TimeoutError:
            pass
        else:
            r2 = mod_nest_exp(seq, m)
            assert r1 == r2