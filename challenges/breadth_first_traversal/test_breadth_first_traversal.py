import pytest
from bst import BST
from breadth_first_traversal import breadth_first_traversal


@pytest.fixture
def empty_bst():
    """make empty bst"""
    return BST()


@pytest.fixture
def small_bst():
    return BST([4, 2, 3, 1, 5, 6, 7])

@pytest.fixture
def min_bst():
    return BST([3, 1, 4])


def test_empty_tree(empty_bst):
    """check case of empty tree"""
    a = []
    assert breadth_first_traversal(empty_bst, a.append) is False


def test_min_tree_(min_bst):
    """CHECK SMALL BT"""
    a = []
    breadth_first_traversal(min_bst, a.append)
    assert a == [3, 1, 4]


def test_min_tree(small_bst):
    """CHECK BIG TREE"""
    a = []
    breadth_first_traversal(small_bst, a.append)
    assert a == [4, 2, 5, 1, 3, 6, 7]
