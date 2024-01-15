from setuptools import setup, Extension
from Cython.Build import cythonize

import os

HERE = os.path.dirname(__file__)

packages = ["pybash", "pybash.sh_reader", "pybash.commands"]

with open(os.path.join(HERE, "README.md")) as f:
    DESCRIPTION = f.read()

def package_data(packages, *types):
    value:dict[str, list[str]] = dict()

    for package in packages:
        value[package] = []
        for type in types:
            value[package].append(f"*.{type}")
    
    return value

def find_files(packages:list[str]):
    for package in packages:
        where = package.replace(os.extsep, os.sep)
        with os.scandir(where) as iterator:
            for item in iterator:
                if item.is_dir():
                    continue

                if item.name.endswith(".pyx"):
                    yield Extension(
                        package + os.extsep + item.name[0:-4]
                    )

setup(
    name="pybash",
    version="1.0.0",
    author="Filipi565",
    description="a simple Windows bash shell",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Cython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 11",
    ],
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    python_requires = ">=3.8",
    project_urls = {
        "Source": "https://github.com/Filipi565/LipiUtils",
        "Issues": "https://github.com/Filipi565/LipiUtils/issues",
    },
    packages=packages,
    package_data=package_data(packages, "py", "exe", "pyi"),
    ext_modules=cythonize(list(find_files(packages)))
)