#!/usr/bin/env python
"""Setup logic for pip."""

from setuptools import setup

setup(
    name='automata_python',
    version='0.0.3',
    description='Python Automata Library',
    url='https://github.com/hemangsk/automata-python',
    author='Hemang Kumar',
    author_email='hemangsk@gmail.com',
    license='GPLv3',
    keywords='language finite automata turing machine push down automata linear bound automata',
    packages=[
        'automata'
    ],
    install_requires=[],
    entry_points={}
)
