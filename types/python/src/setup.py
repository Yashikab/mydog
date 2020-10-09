# coding: utf-8
# python: 3.7
from setuptools import setup

setup(
    name="mydog_python",
    entry_points={
        "console_scripts": [
            "rp_reviewdog = rp_reviewdog:main",
            "rp_pytest=rp_pytest:main"
        ]
    }
)
