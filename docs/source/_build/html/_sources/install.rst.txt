Installation
============

PyPI
^^^^

``mod-nest-exp`` is hosted on GitHub, but the easiest way to install it is to download
the latest release from its `PyPI repository <https://pypi.org/project/mod-nest-exp/>`_:

.. code:: console

	$ pip install --user mod-nest-exp


GitHub + ``pip``
^^^^^^^^^^^^^^^^

If, for any reason, you prefer to download the library from GitHub, you can clone
the repository and install the repository by running (with the admin rights):

.. code:: console

	$ pip install --user https://github.com/avivbrook/modular-nested-exponentiation/archive/master.zip

Keep in mind this will install the development version of the library, so not
everything may work as expected compared to a stable release.


GitHub + ``setuptools``
^^^^^^^^^^^^^^^^^^^^^^^

If you do not have ``pip`` installed, you can still clone the repository and
run the ``setup.py`` file manually:

.. code:: console

	$ git clone https://github.com/avivbrook/modular-nested-exponentiation.git
	$ cd modular-nested-exponentiation
	# python setup.py install
