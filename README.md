## dsv

[![Build Status](https://travis-ci.org/kootenpv/dsv.svg?branch=master)](https://travis-ci.org/kootenpv/dsv)
[![PyPI](https://img.shields.io/pypi/v/dsv.svg?style=flat-square)](https://pypi.python.org/pypi/dsv/)
[![PyPI](https://img.shields.io/pypi/pyversions/dsv.svg?style=flat-square)](https://pypi.python.org/pypi/dsv/)

### Initial flow

Read/write automagically "Delimiter" Seperated Value files. The delimiter will be inferred from the file.

Functionality:

    import dsv
    obj = ["1", "2", "3"]
    dsv.write(obj, "fname.csv")
    new_obj = dsv.read(obj, "fname.csv")
    assert obj == new_obj

It supports iterative read as well using `iread`.

### Included in

- [just](https://github.com/kootenpv/just)
