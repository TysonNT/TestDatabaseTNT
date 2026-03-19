[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "matprotlib" # OR "test-database-3"
version = "0.0.1"
authors = [
  { name="Tyson Tran", email="tyson26tran@gmail.com },
]
description = "A clean and simple material property database."
readme = "README.md"
requires-python = ">=3.7"
dependencies = [
    "numpy", # This tells pip to automatically install numpy if the user doesn't have it!
]
classifiers = [
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
]
