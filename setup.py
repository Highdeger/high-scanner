# !/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# Package meta-data
NAME = 'highscanner'
DESCRIPTION = 'A simple port scanner with no dependencies'
URL = 'https://github.com/Highdeger/HighPortScanner'
EMAIL = 'highdeger@gmail.com'
AUTHOR = 'Highdeger'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = None
LICENSE = 'GPLv3'
REQUIRED = []

with open('README.md', mode='r') as f:
    long_description = '\n' + f.read()

about = {}
if not VERSION:
    with open('__version__.py', mode='r') as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

setup(
    name=NAME,
    version=about['__version__'],
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=URL,
    packages=find_packages(),
    license=LICENSE,
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: System :: Networking'
    ],
    python_requires='>=3.5',
)
