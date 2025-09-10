from setuptools import setup

setup(
    name="fileora",
    version="1.0",
    py_modules=["fileora"],
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "fileora=fileora:main",
        ],
    },
)
