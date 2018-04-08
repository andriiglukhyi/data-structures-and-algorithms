import pytest
from .bst import BST
from .bst import Node as nd


@pytest.fixture
def empty_bst():
    """make empty bst"""
    return BST()


@pytest.fixture
def node():
    """make node"""
    return nd(5)
 

@pytest.fixture
def small_bst():
    return BST([4, 3, 3.5, 2, 5, 6, 7])


def test_constractor(empty_bst):
    """test constarctor"""
    assert empty_bst.root is None


def test_node(node):
    """test node object"""
    assert node.right is None
    assert node.left is None


def test_value_of_node(node):
    """test repr and str of node"""
    assert node.val == 5


def test_insert_empty(empty_bst):
    """insert in empty bst"""
    empty_bst.insert(5)
    assert empty_bst.root.val == 5


def test_insert_empty_two(empty_bst):
    """insert two items"""
    empty_bst.insert(3)
    empty_bst.insert(10)
    assert empty_bst.root.val == 3
    assert empty_bst.root.right.val == 10
    assert empty_bst.root.left is None


def test_repr_small_bst(small_bst):
    """test repr of small bst"""
    assert small_bst.root.val == 4
    assert small_bst.root.right.val == 5


def test_insert_for_small_bst(small_bst):
    """test insert in small bst"""
    small_bst.insert(1)
    small_bst.insert(1.5)
    assert small_bst.root.left.val == 3
    assert small_bst.root.right.val == 5


def test_inorder_traverse(small_bst):
    """test in order tarversal"""
    a = []
    small_bst.in_order(a.append)
    assert a == [2, 3, 3.5, 4, 5, 6, 7]


def test_pre_order(small_bst):
    """test preorder traversal"""
    a = []
    small_bst.pre_order(a.append)
    assert a == [4, 3, 2, 3.5, 5, 6, 7]


def test_post_order(small_bst):
    """test preorder"""
    a = []
    small_bst.post_order(a.append)
    assert a == [2, 3.5, 3, 7, 6, 5, 4]