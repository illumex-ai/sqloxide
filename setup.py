# -*- coding: utf-8 -*-
from setuptools import setup

packages = ["sqloxide"]

package_data = {"": ["*"]}

setup_kwargs = {
    "name": "sqloxide",
    "version": "0.2.26",
    "description": "Python bindings for sqlparser-rs",
    "long_description": open("readme.md").read(),
    "long_description_content_type": "text/markdown",
    "author": "illumex",
    "author_email": "yuval@illumex.ai",
    "maintainer": None,
    "maintainer_email": None,
    "url": "https://github.com/illumex-ai/sqloxide",
    "packages": packages,
    "package_data": package_data,
    "python_requires": ">=3.7,<4.0",
}
from build import *

build(setup_kwargs)

setup(**setup_kwargs)
