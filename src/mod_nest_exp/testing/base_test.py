from typing import Callable, Iterable
from time import time
from .utils import all_equal

def _trial(function: Callable, args: Iterable):
    start_time = time()
    result = function(*args)
    end_time = time()
    return {
        'result': result,
        'time': end_time - start_time
    }

def benchmark(
    functions: list[Callable],
    arguments: Iterable,
    validate: bool = False,
    max_iters: int = None,
    max_seconds: int = None,
):
    times = {function: list() for function in functions}
    start_time = time()
    for i, args in enumerate(arguments):
        results = dict()
        for function in functions:
            trial = _trial(function, args)
            results[function] = trial['result']
            times[function].append(trial['time'])
        if validate:
            if not all_equal(results.values()):
                raise AssertionError('Outputs not all equal')
        elapsed_time = time() - start_time
        if max_iters is not None and i+1 >= max_iters:
            break
        if max_seconds is not None and elapsed_time >= max_seconds:
            break
    return times