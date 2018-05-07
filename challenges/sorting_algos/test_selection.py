from selection import sorting_algos
import pytest

@pytest.fixture
def small_array():
    small_array = [10, 9, 7, 100, 26, 85]
    return small_array


@pytest.fixture
def duplicate_array():
    small_array = [10, 9, 10, 10, 10, -1]
    return small_array


@pytest.fixture
def super_small():
    super_small = [1]
    return super_small

@pytest.fixture
def small():
    super_small = [10, 3, 9]
    return super_small


def test_super_small_array(super_small):
    """check when array is too small"""
    assert sorting_algos(super_small) == [1]


def test_small_array(small):
    """check when array is too small"""
    assert sorting_algos(small) == [3, 9, 10]


def test_big_array_(small_array):
    """check bigger array"""
    assert sorting_algos(small_array) == sorted(small_array)


def test_big_array(duplicate_array):
    """check array with duplicates"""
    assert sorting_algos(duplicate_array) == sorted(duplicate_array)
