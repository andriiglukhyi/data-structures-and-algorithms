from bst import BST
import pytest
from tree_intersection import tree_intersection


@pytest.fixture
def empty_bst():
    """make empty bst"""
    return BST()


@pytest.fixture
def small_bst():
    return BST([4, 3, 3.5, 2, 5, 6, 7])


@pytest.fixture
def big_bst():
    return BST([4, 2, 2.5, -1, 5, 6, 7])


@pytest.fixture
def ss_bst():
    return BST([1, 2, 6, 0, 7, 4, 2])


def test_empty_tree(empty_bst, small_bst):
    """tests if one tree empty"""
    assert tree_intersection(empty_bst, small_bst) is False


def test_small_bst(small_bst, big_bst):
    """test correct answear"""
    assert tree_intersection(small_bst, big_bst) == [2, 4, 5, 6, 7]

