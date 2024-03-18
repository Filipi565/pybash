from setuptools import setup, find_packages
import os

HERE = os.path.abspath(os.path.dirname(__file__))

packages = find_packages(os.path.join(HERE, "src"))

def package_data(packages, *types): # type: (list[str], str) -> dict[str, list[str]]
    value = dict() # type: dict[str, list[str]]

    for package in packages:
        value[package] = []
        for type in types:
            value[package].append(f"*.{type}")
    
    return value

setup(
    package_data=package_data(packages, "py", "exe", "pyi"),
)