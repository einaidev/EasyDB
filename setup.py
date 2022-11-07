from setuptools import setup, find_packages
from Cython.Build import cythonize
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    ext_modules=cythonize("./EasyDB/C/cmiscs.pyx"),
    name="EasyDB.py",
    version="1.2.3",
    author="Nando Msc",
    packages=find_packages(),
    requires=["Cython"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.10',
    keywords=["DataBase", "DB", "Json"],
    long_description=long_description,
    long_description_content_type='text/markdown',
    project_urls={
        "Home Page": "https://github.com/einaidev/EasyDB",
        "GitHub": "https://github.com/einaidev",
        "Documentation": "https://github.com/einaidev/EasyDB/blob/main/README.md"
    },
    description="A very easy database but very good :)"
)