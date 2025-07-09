#!/usr/bin/env python3

from setuptools import setup

setup(
    name="mgit",
    version="0.1.1",
    packages=["mgit"],
    entry_points={"console_scripts": ["mgit=mgit.cli:main"]},
)
