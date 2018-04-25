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
    small_tree.insert(1, 10)
    small_tree.insert(2, 10)
    return small_tree


def test_print_level_order_empty_tree(empty_k_tree):
    """test empty tree"""
    assert pl(empty_k_tree) is False


def test_print_level_order_small_tree(small_k_tree):
    """test small tree"""
    print(pl(small_k_tree))
    assert pl(small_k_tree) == ''
