# Modular nested exponentiation

An algorithm that computes modular nested exponentiation efficiently.

[![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/avivbrook/modular-nested-exponentiation/Test/master?logo=github&style=flat-square)](https://github.com/avivbrook/modular-nested-exponentiation/actions)
[![PyPI - License](https://img.shields.io/pypi/l/mod-nest-exp?style=flat-square)](https://choosealicense.com/licenses/gpl-3.0/)
[![PyPI](https://img.shields.io/pypi/v/mod-nest-exp?style=flat-square)](https://pypi.org/project/mod-nest-exp/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mod-nest-exp?style=flat-square)](https://pypi.org/project/mod-nest-exp/#files)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/mod-nest-exp?style=flat-square)](https://pypi.org/project/mod-nest-exp/#files)
[![GitHub issues](https://img.shields.io/github/issues/avivbrook/modular-nested-exponentiation?style=flat-square)](https://github.com/avivbrook/modular-nested-exponentiation/issues)
[![codecov](https://codecov.io/gh/avivbrook/modular-nested-exponentiation/branch/master/graph/badge.svg?token=5CWMO8OLNU)](https://codecov.io/gh/avivbrook/modular-nested-exponentiation)
[![Downloads](https://img.shields.io/badge/dynamic/json?style=flat-square&color=303f9f&label=downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fmod-nest-exp)](https://pepy.tech/project/mod-nest-exp)

## 🚩 Table of Contents
- [Overview](#%EF%B8%8F-overview)
- [Prerequisites](#%EF%B8%8F-prerequisites)
- [Installation](#-installation)
- [Examples](#-examples)

## 🗺️ Overview

`mod-nest-exp` exports a Python function `mod_nest_exp` that takes as input an arbitrarily long sequence of positive integers `a₁, a₂, ..., aₙ` and a positive integer `m` and computes `a₁^(a₂^(···^aₙ)) mod m` efficiently (that is, without computing the value of the nested exponent).

## 🏳️ Prerequisites

`mod-nest-exp` requires Python v3.6+.

For best performance, install `gmpy2` and `sympy`:
```console
$ apt install libgmp-dev libmpfr-dev libmpc-dev # required for gmpy2
$ pip install gmpy2 sympy
```

The libraries offer more efficient alternatives to a number of functions used as subroutines in the core module.

## 🔧 Installation

The recommended installation method is from [PyPI](https://pypi.org/project/mod-nest-exp/):
```console
$ pip install mod-nest-exp
```

A development version can be installed from GitHub source using `setuptools`:
```console
$ git clone https://github.com/avivbrook/modular-nested-exponentiation.git
$ cd modular-nested-exponentiation
$ python setup.py install
```

## 💡 Examples

### Small inputs

```python
>>> from mod_nest_exp import mod_nest_exp
>>> mod_nest_exp([6,5,4,3,2], 1948502738) # 6^(5^(4^(3^2))) mod 1948502738
951546056
```

### Larger inputs

Here we demonstrate a computation that is not possible with simple modular exponentiation functions such as `pow`:
```python
>>> from random import randint
>>> seq = [randint(1, 2**64) for _ in range(5)]
>>> seq
[6038140174510300905, 11769918488496772646, 2874847465098133786, 9008748983185995190, 13009674817390511365]
>>> m = randint(1, 2**64)
>>> m
6790053138492639247
>>> mod_nest_exp(seq, m)
3426314670852891859
```

### Benchmark the main function

```python
>>> from mod_nest_exp.core.benchmarks import benchmark_core
>>> benchmark_core(list_lengths=(10, 100, 1000), bit_lengths=(16, 128, 1024), mod_bit_lengths=(16, 32, 64))
Running mod_nest_exp on sequences of l pseudorandom b-bit positive integers over a B-bit modulus (1000 runs per table entry)
=================================================================
                            sequence length l
                  10               100               1000
          ----------------- ----------------- -----------------
  B     b     mean    stdev     mean    stdev     mean    stdev
-----------------------------------------------------------------
       16 |   0.08     0.04     0.08     0.03     0.10     0.03
 16   128 |   0.08     0.11     0.08     0.03     0.10     0.04
     1024 |   0.08     0.03     0.08     0.03     0.11     0.04
-----------------------------------------------------------------
       16 |   0.34     0.32     0.34     0.24     0.35     0.24
 32   128 |   0.33     0.23     0.34     0.23     0.36     0.23
     1024 |   0.33     0.22     0.33     0.24     0.37     0.24
-----------------------------------------------------------------
       16 |   8.82    34.83     6.20    21.27     7.18    30.35
 64   128 |   7.66    30.70     6.71    22.72     7.60    26.92
     1024 |   5.94    25.10     6.67    20.78     6.76    26.28
=================================================================
```