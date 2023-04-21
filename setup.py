import os
from setuptools import setup

root_folder = "./src"


def get_packages() -> list[str]:
    return [
        f"src.{name}"
        for name in os.listdir(root_folder)
        if os.path.isdir(os.path.join(root_folder, name)) and name != "__pycache__"
    ]


setup(
    name="src",
    include_package_data=True,
    description="All showcode challenges",
    packages=get_packages(),
)
