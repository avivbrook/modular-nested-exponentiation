``modular-nested-exponentiation``
=================================

An algorithm that computes modular nested exponentiation efficiently.

|License| |Source| |Coverage| |PyPI| |Versions| |Downloads|

.. |License| image:: https://img.shields.io/pypi/l/mod-nest-exp?style=flat-square
   :target: https://choosealicense.com/licenses/gpl-3.0/

.. |Source| image:: https://img.shields.io/badge/source-GitHub-303030.svg?style=flat-square
   :target: https://github.com/avivbrook/modular-nested-exponentiation/

.. |Coverage| image:: https://codecov.io/gh/avivbrook/modular-nested-exponentiation/branch/master/graph/badge.svg?token=5CWMO8OLNU
   :target: https://codecov.io/gh/avivbrook/modular-nested-exponentiation

.. |PyPI| image:: https://img.shields.io/pypi/v/mod-nest-exp?style=flat-square
   :target: https://pypi.org/project/mod-nest-exp/

.. |Versions| image:: https://img.shields.io/pypi/pyversions/mod-nest-exp?style=flat-square
   :target: https://pypi.org/project/mod-nest-exp/#files

.. |Downloads| image:: https://img.shields.io/badge/dynamic/json?style=flat-square&color=303f9f&label=downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fmod-nest-exp
   :target: https://pepy.tech/project/mod-nest-exp

``mod-nest-exp`` exports a Python function ``mod_nest_exp`` that takes as input an arbitrarily long sequence of positive integers ``a₁, a₂, ..., aₙ`` and a positive integer ``m`` and computes ``a₁^(a₂^(···^aₙ)) mod m`` efficiently (that is, without computing the value of the nested exponent).

To date, this problem was not solvable by computers in the general case.

Setup
-----

Run ``pip install mod-nest-exp`` in a shell to download the latest release from PyPI, or have a look at the
:doc:`Installation page <install>` to find other ways to install ``mod-nest-exp``.

.. note::

   ``mod-nest-exp`` requires Python v3.6+. For best performance, install ``gmpy2`` and ``sympy``:

   .. code:: console

      $ apt install libgmp-dev libmpfr-dev libmpc-dev # required for gmpy2
      $ pip install gmpy2 sympy

Library
-------

.. toctree::
   :maxdepth: 2

   Installation <install>
   To-do <todo>
   About <about>

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`