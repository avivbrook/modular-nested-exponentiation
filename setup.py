import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='mod-nest-exp',
    version='1.0.6',
    author='Aviv Brook',
    author_email='avbrook@ucsc.edu',
    description='An algorithm that computes modular nested exponentiation efficiently',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/avivbrook/modular-nested-exponentiation',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Operating System :: OS Independent'
    ],
    package_dir={'': 'src'},
    install_requires=['sympy'],
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.6'
)