# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup(
    name="Reproductor de youtube Python",
    version="1.0",
    description="",
    author="fmart",
    author_email="fmartinvillegas00@gmail.com",
    url="https://github.com/franmartinv/reproductor_python",
    license="libre",
    scripts=["VLC-python-script.py"],
    console=["VLC-python-script.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)