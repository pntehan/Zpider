# -*- coding:utf-8 -*-
# author:Pntehan


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Zpider-pkg-YOUR-PNTEHAN-HERE",
    version="0.0.1",
    author="pntehan",
    author_email="pntehan@gmail.com",
    description="Use socket",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
