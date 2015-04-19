#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="reddit",
    version="0.1.0",
    author="wen",
    author_email="kwen717@gmail.com",
    packages=[
        "reddit",
    ],
    include_package_data=True,
    install_requires=[
        "Django==1.7.6",
    ],
    zip_safe=False,
    scripts=["reddit/manage.py"],
)
