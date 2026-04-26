from setuptools import setup

import os
BASEPATH = os.path.dirname(os.path.abspath(__file__))

from setuptools import setup, find_packages

setup(
    name="onmt",
    version="0.0.0",
    packages=find_packages(),  # will find the onmt/ package at root
)
