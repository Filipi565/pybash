from setuptools import setup

packages = ["pybash", "pybash.sh_reader", "pybash.commands"]

def package_data(packages, *types):
    value = dict() # type: dict[str, list[str]]

    for package in packages:
        value[package] = []
        for type in types:
            value[package].append(f"*.{type}")
    
    return value

setup(
    packages=packages,
    package_data=package_data(packages, "py", "exe", "pyi"),
)