import pytest

import main


def test_get_1():
    assert main.get([1, 2, 3], 2, default="test") == 3


def test_get_2():
    with pytest.raises(IndexError):
         main.get([], 0, default="test") == "test"


def test_slice_1():
    assert main.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]


def test_slice_2():
    assert main.my_slice([1, 2, 3], 1) == [2, 3]
