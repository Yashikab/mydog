# coding: utf-8
# python: 3.7
from setuptools import setup

setup(
    name="mydog_python",
    entry_points={
        "console_scripts": [
            "rp_reviewdog_py = rp_reviewdog:main"
        ]
    }
)
