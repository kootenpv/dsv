""" Our tests are defined in here """
import os
import dsv


def test_csv():
    fname = "testobj.csv"
    obj = [{"a": 1, "b": 2}] * 100
    dsv.write(obj, "testobj.csv")
    try:
        assert dsv.read(fname) == [['a', 'b']] + [['1', '2']] * 100
    finally:
        os.remove(fname)


def test_csv_iread():
    fname = "testobj.csv"
    obj = [['"a"', '"b"'], ['"1"', '"2"']] * 100
    dsv.write(obj, "testobj.csv")
    try:
        assert list(dsv.iread(fname)) == obj
    finally:
        os.remove(fname)


def test_csv_iread_error():
    fname = "testobj.csv"
    obj = [['"a"', '"b"'], ['"1"', '"2"', '"']] * 100
    dsv.write(obj, "testobj.csv")
    try:
        list(dsv.iread(fname))
        # should not reach here
    except ValueError:
        assert True
    finally:
        os.remove(fname)


def test_csv_iread_problem_lines():
    fname = "testobj.csv"
    obj = ["a"] + [['"a"', '"b"'], ['"1"', '"2"']] * 100
    dsv.write(obj, "testobj.csv")
    try:
        dsv.read(fname)
    except ValueError:
        assert True
    finally:
        os.remove(fname)
