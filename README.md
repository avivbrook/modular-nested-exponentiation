# modular-nested-exponentiation

An algorithm that computes modular nested exponentiation efficiently.

<table>
    <tr>
        <td>License</td>
        <td><img src='https://img.shields.io/pypi/l/mod-nest-exp.svg'></td>
        <td>Version</td>
        <td><img src='https://img.shields.io/pypi/v/mod-nest-exp.svg'></td>
    </tr>
    <tr>
        <td>Wheel</td>
        <td><img src='https://img.shields.io/pypi/wheel/mod-nest-exp.svg'></td>
        <td>Implementation</td>
        <td><img src='https://img.shields.io/pypi/implementation/mod-nest-exp.svg'></td>
    </tr>
    <tr>
        <td>Status</td>
        <td><img src='https://img.shields.io/pypi/status/mod-nest-exp.svg'></td>
        <td>Supported versions</td>
        <td><img src='https://img.shields.io/pypi/pyversions/mod-nest-exp.svg'></td>
    </tr>
    <!-- <tr>
        <td>Downloads</td>
        <td><img src='https://img.shields.io/pypi/dm/mod-nest-exp.svg'></td>
    </tr> -->
</table>

## Generalised modular exponentiation

We present an algorithm that takes as input an arbitrarily long sequence of positive integers `a₁, a₂, a₃, ..., aₙ` and a positive integer `m` and computes `a₁^(a₂^(···^aₙ)) mod m` efficiently (that is, without computing the value of the nested exponent).

Without this algorithm, this type of computation is unfeasible for modern computers even for short input sequences containing small integers.

## Prerequisites

```bash
$ apt install libgmp-dev libmpfr-dev libmpc-dev
$ pip install sympy gmpy2
```

## Install

```bash
$ pip install mod-nest-exp
```

## Usage

```bash
$ python
>>> from mod_nest_exp import mod_nest_exp
>>> mod_nest_exp([6, 5, 4, 3, 2], 1948502738)
mpz(951546056) # uses gmpy2 if available
```