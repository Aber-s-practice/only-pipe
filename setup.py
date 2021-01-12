#!/usr/bin/python3
import os
from setuptools import setup


with open("./README.md", "r", encoding="utf8") as file:
    long_description = file.read()


setup_kwargs = {
    "name": "only-pipe",
    "version": "1.0.0",
    "description": "A non-intrusive Python pipeline.",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "author": "abersheeran",
    "author_email": "me@abersheeran.com",
    "url": "https://github.com/abersheeran/only-pipe",
    "license": "MIT",
    "classifiers": [
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    "py_modules": ["pipe"],
}

setup(**setup_kwargs)
