#!/usr/bin/env python
"""Setup logic for pip."""

from setuptools import setup

setup(
    name='automata_python',
    version='0.0.1',
    description='The only automaton library you will ever need',
    long_description=get_long_description(),
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
