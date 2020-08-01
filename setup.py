#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

try:
    # pip >=20
    from pip._internal.network.session import PipSession
    from pip._internal.req import parse_requirements
except ImportError:
    try:
        # 10.0.0 <= pip <= 19.3.1
        from pip._internal.download import PipSession
        from pip._internal.req import parse_requirements
    except ImportError:
        # pip <= 9.0.3
        from pip.download import PipSession
        from pip.req import parse_requirements

list_requirements = [str(ir.req) for ir in parse_requirements('requirements.txt', session=PipSession())]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mop-suit",
    version="0.0.1",
    entry_points={
        'console_scripts': ['mop=mop:main'],
    },
    author="Oleg Silver",
    author_email="rav-navini-gego-cutropal@yandex.ru",
    description="Полезная утилита, призванная сделать ваш python проект чище",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ogurechik/mop",
    packages=find_packages(),
    install_requires=list_requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license='MIT',
)
