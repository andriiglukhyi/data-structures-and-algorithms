import pytest
from .k_tree import KTree
from .k_tree import Node


@pytest.fixture
def empty_k_tree():
    """make empty k_tree"""
    return KTree()


@pytest.fixture
def small_k_tree():
    """make empty k_tree"""
    small_tree = KTree()
    small_tree.insert(1)
    small_tree.insert(2)
    return small_tree


@pytest.fixture
def node_k_tree():
    """make small k_tree"""
    return Node(4)


def test_node_root(node_k_tree):
    """test node class"""
    assert node_k_tree.val == 4
    assert node_k_tree.children == []


def test_empty_ktree(empty_k_tree):
    """assert empty node hase toot equal to none"""
    assert empty_k_tree.root is None


def test_empty_ktree_insert(empty_k_tree):
    """insert one item in tree"""
    empty_k_tree.insert(4)
    assert empty_k_tree.root.val == 4
    assert len(empty_k_tree.root.children) == 0


def test_small_k_tree(small_k_tree):
    """test small tree instance"""
    assert small_k_tree.root.val == 1
    assert small_k_tree.root.children[0].val == 2
    assert len(small_k_tree.root.children) == 1


def test_empty_ktree_insert_multi(empty_k_tree):
    """test empty tree insrtation"""
    empty_k_tree.insert(8)
    assert empty_k_tree.root.val == 8
    assert len(empty_k_tree.root.children) == 0
    empty_k_tree.insert(10, 8)
    assert empty_k_tree.root.children[0].val == 10
    assert len(empty_k_tree.root.children) == 1


def test_small_k_tree_insert_multi(small_k_tree):
    """insert multi elements in small_k_tree"""
    small_k_tree.insert(10, 1)
    assert small_k_tree.root.children[0].val == 2
    assert small_k_tree.root.children[1].val == 10
    # import pdb; pdb.set_trace()
    small_k_tree.insert(5, 10)
    assert len(small_k_tree.root.children[1].children) == 1


def test_small_k_tree_breadth_first(small_k_tree):
    """check breadth first for small tree"""
    small_k_tree.insert(10, 1)
    small_k_tree.insert(5, 10)
    small_k_tree.insert(3, 10)
    a = []
    small_k_tree.breadth_first_traversal(a.append)
    assert len(a) == 5


def test_empty_k_tree_breadth_first(empty_k_tree):
    """test breadth first for empty tree"""
    a = []
    assert empty_k_tree.breadth_first_traversal(a.append) is False


def test_preorder(small_k_tree):
    """test preorder traversal"""
    small_k_tree.insert(10, 1)
    a = []
    small_k_tree.pre_order(a.append)
    assert a == [1, 2, 10]
    b = []
    small_k_tree.insert(5, 10)
    small_k_tree.insert(3, 10)
    small_k_tree.pre_order(b.append)
    assert b == [1, 2, 10, 5, 3]


def test_post_orer(small_k_tree):
    small_k_tree.insert(10, 1)
    a = []
    small_k_tree.post_order(a.append)
    assert a == [2, 10, 1]
    b = []
    small_k_tree.insert(5, 10)
    small_k_tree.insert(3, 10)
    small_k_tree.post_order(b.append)
    assert b == [2, 5, 3, 10, 1]