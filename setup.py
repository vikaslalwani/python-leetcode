# coding: utf-8

"""
    Leetcode API

    Leetcode API implementation.  # noqa: E501

    OpenAPI spec version: 1.0.1-1
    Contact: pv.safronov@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
from __future__ import annotations

from setuptools import find_packages, setup  # noqa: H301

NAME = "python-leetcode"
VERSION = "1.1.0"

with open("README.md") as readme:
    DESCRIPTION: str = readme.read()

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil", "requests"]

setup(
    name=NAME,
    version=VERSION,
    description="Leetcode API",
    author="Pavel Safronov",
    author_email="pv.safronov@gmail.com",
    url="https://github.com/prius/python-leetcode",
    keywords=["leetcode", "faang", "interview", "api"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.8",
)
