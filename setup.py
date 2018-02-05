#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: No Input/Output (Daemon)',
    'Intended Audience :: System Administrators',
    'Natural Language :: English',
    'Operating System :: POSIX',
    'Topic :: System :: Boot',
    'Topic :: System :: Monitoring',
    'Topic :: System :: Systems Administration',
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
]


setup(
    name="supervisor-quick",
    version=__import__("supervisor_quick").__version__,
    description="Bypass supervisor's nasty callbacks stack and make it quick!",
    classifiers=CLASSIFIERS,
    author="Lx Yu",
    author_email="i@lxyu.net",
    py_modules=["supervisor_quick", ],
    package_data={"": ["LICENSE"], },
    url="http://lxyu.github.io/supervisor-quick/",
    license="MIT",
    long_description=open("README.rst").read(),
    install_requires=[
        "supervisor",
        "future",
    ],
)
