from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("./EasyDB/C/cmiscs.pyx"),
    name="EasyDB",
    version="1.0.0",
    packages=find_packages()
)