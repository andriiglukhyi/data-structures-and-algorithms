from k_tree import KTree, Node
from find_matches import find_matches
import pytest


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
    big_tree.insert(10)
    big_tree.insert(10, 10)
    big_tree.insert(10, 10)
    return big_tree


def test_empty_tree(empty_k_tree):
    """test empty tree"""
    assert find_matches(empty_k_tree, 10) is False
    assert find_matches(empty_k_tree) is False


def test_small_tree(small_k_tree):
    """test small tree"""
    assert find_matches(small_k_tree, 10)[0].val == 10
    a = find_matches(small_k_tree, 10)
    assert len(a) == 1


def test_big_tree(big_k_tree):
    """test multiply number"""
    assert find_matches(big_k_tree, 10)[0].val == 10
    assert find_matches(big_k_tree, 10)[1].val == 10
    assert find_matches(big_k_tree, 10)[2].val == 10
    assert len(find_matches(big_k_tree, 10)) == 3
    