import pytest
from print_level_order import print_level_order as pl
from k_tree import KTree


@pytest.fixture
def empty_k_tree():
    """make empty k_tree"""
    return KTree()


@pytest.fixture
def small_k_tree():
    """make small k_tree"""
    small_tree = KTree()
    small_tree.insert(1)
    small_tree.insert(2)
    small_tree.insert(10, 1)
    return small_tree


@pytest.fixture
def big_k_tree():
    """make small k_tree"""
    big_tree = KTree()
    big_tree.insert(1)
    big_tree.insert(2)
    big_tree.insert(3)
    big_tree.insert(4, 2)
    big_tree.insert(5, 2)
    big_tree.insert(6, 2)
    big_tree.insert(7, 3)
    return big_tree


def test_print_level_order_empty_tree(empty_k_tree):
    """test empty tree"""
    assert pl(empty_k_tree) is False


def test_print_level_order_small_tree(small_k_tree):
    """test small tree"""
    assert pl(small_k_tree)[:-4] == '1 \n 2 10  \n'


def test_print_velel_big_tree(big_k_tree):
    """test big tree"""
    assert pl(big_k_tree)[:-4] == '1 \n 2 3  \n 4 5 6 7'
