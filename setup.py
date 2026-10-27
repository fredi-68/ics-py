#!/usr/bin/env python
import sys

from setuptools import setup

#from ics.__meta__ import __author__, __license__, __title__, __version__

# fuck it
__title__ = "ics"
__version__ = "0.7.4"
__author__ = "Nikita Marchant"
__license__ = "Apache License, Version 2.0"
__copyright__ = "Copyright 2013-2020 Nikita Marchant and individual contributors"

with open("requirements.txt") as f:
    install_requires = [line for line in f if line and line[0] not in "#-"]

with open("dev/requirements-test.txt") as f:
    tests_require = [line for line in f if line and line[0] not in "#-"]


def readme():
    with open('README.rst', encoding='utf-8') as f:
        return f.read()


setup(
    name=__title__,
    version=__version__,
    description='Python icalendar (rfc5545) parser',
    long_description=readme(),
    keywords='ics icalendar calendar event todo rfc5545 parser pythonic',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Scheduling',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Typing :: Typed',

    ],
    url='http://github.com/C4ptainCrunch/ics.py',
    author=__author__,
    author_email='nikita.marchant@gmail.com',
    install_requires=install_requires,
    license=__license__,
    packages=['ics'],
    include_package_data=True,
    zip_safe=False,
)
