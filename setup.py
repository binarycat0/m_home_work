#!/usr/bin/env python

from os.path import join, dirname

import app
from setuptools import setup, find_packages

root = dirname(__file__)

setup(
    name='m_home_work ',
    version=app.__version__,
    packages=find_packages(),
    long_description=open(join(root, 'README.txt')).read(),

    entry_points={
        'console_scripts': [
            'm_home_work = app.home_work:main',
        ]
    },
)
