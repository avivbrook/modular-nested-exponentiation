# modular-nested-exponentiation

An algorithm that computes modular nested exponents (or towers) efficiently.

[![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/avivbrook/modular-nested-exponentiation/Test/master?logo=github&style=flat-square)](https://github.com/avivbrook/modular-nested-exponentiation/actions)
[![PyPI - License](https://img.shields.io/pypi/l/mod-nest-exp?style=flat-square)](https://choosealicense.com/licenses/gpl-3.0/)
[![PyPI](https://img.shields.io/pypi/v/mod-nest-exp?style=flat-square)](https://pypi.org/project/mod-nest-exp/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mod-nest-exp?style=flat-square)](https://pypi.org/project/mod-nest-exp/#files)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/mod-nest-exp?style=flat-square)](https://pypi.org/project/mod-nest-exp/#files)
[![GitHub issues](https://img.shields.io/github/issues/avivbrook/modular-nested-exponentiation?style=flat-square)](https://github.com/avivbrook/modular-nested-exponentiation/issues)
[![Downloads](https://img.shields.io/badge/dynamic/json?style=flat-square&color=303f9f&label=downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fmod-nest-exp)](https://pepy.tech/project/mod-nest-exp)

## 🚩 Table of Contents

- [Overview](#%EF%B8%8F-overview)
- [Prerequisites](#%EF%B8%8F-prerequisites)
- [Installation](#-installation)
- [Examples](#-examples)

## 🗺️ Overview

`mod-nest-exp` exports a Python function `mod_nest-exp` that takes as input an arbitrarily long sequence of positive integers `a₁, a₂, ..., aₙ` and a positive integer `m` and computes `a₁^(a₂^(···^aₙ)) mod m` efficiently (that is, without computing the value of the nested exponent).

## 🏳️ Prerequisites

`sympy` is currently required as the algorithm uses its `totient` function. In the future, a custom totient function will be added so that `sympy` is not required, making the module self-contained.

For best performance, install `gmpy2`:
```console
$ apt install libgmp-dev libmpfr-dev libmpc-dev # required for gmpy2
$ pip install gmpy2
```

`gmpy2` is not required but it offers more efficient versions of some of Python's built-in math functions. If `gmpy2` is not installed, the module simply uses the built-in functions.

## 🔧 Installation

Installing with `pip` is the easiest:
```console
$ pip install mod-nest-exp
```

A development version can be installed from GitHub
using `setuptools`, provided you have `sympy` installed already:
```console
$ git clone https://github.com/avivbrook/modular-nested-exponentiation
$ cd modular-towers
$ python setup.py install
```

## 💡 Examples

```python
>>> from mod_nest_exp import mod_nest_exp
>>> mod_nest_exp([6,5,4,3,2], 1948502738) # 6^(5^(4^(3^2))) mod 1948502738
951546056
```

To benchmark the main function:
```python
>>> from mod_nest_exp.core.tests import test_core
>>> test_core(list_lengths=(10, 100, 1000), bit_lengths=(16, 128, 1024), mod_bit_lengths=(16, 32, 64))
```