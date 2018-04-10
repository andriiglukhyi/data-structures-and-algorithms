import pytest
from bst import BST
from fizzbuzztree import fizz_buzz_tree


@pytest.fixture
def empty_bst():
    """make empty bst"""
    return BST()


@pytest.fixture
def small_bst():
    return BST([4, 3, 3.5, 2, 5, 6, 7])

@pytest.fixture
def min_bst():
    return BST([3, 5, 15, 45])


def test_inorder_traverse(small_bst):
    """test in order tarversal"""
    a = []
    new_tree = fizz_buzz_tree(small_bst)
    new_tree.in_order(a.append)
    assert a == [2, "Fizz", 3.5, 4, "Buzz", 'Fizz', 7]


def test_post_order(min_bst):
    """test small bst"""
    a = []
    new_tree = fizz_buzz_tree(min_bst)
    new_tree.in_order(a.append)
    assert a == ['Fizz', 'Buzz', 'FizzBuzz', 'FizzBuzz']


def test_post_order_(empty_bst):
    """empty bst"""
    assert fizz_buzz_tree(empty_bst) is False
    