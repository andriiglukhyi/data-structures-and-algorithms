from mergesort import mergesort
import pytest

@pytest.fixture
def small_array():
    small_array = [10, 9, 7, 100, 26, 85]
    return small_array


@pytest.fixture
def super_small():
    super_small = [1]
    return super_small

@pytest.fixture
def small():
    super_small = [10, 3, 9]
    return super_small


def test_super_small(super_small):
    """test if array smaller then 2"""
    assert mergesort(super_small) == [1]


def test_small_array(small):
    """test small array with random numbers"""
    assert mergesort(small) == [3, 9, 10]

def test_big_array(small_array):
    """test big array"""
    assert mergesort(small_array) == [7, 9, 10, 26, 85, 100]

