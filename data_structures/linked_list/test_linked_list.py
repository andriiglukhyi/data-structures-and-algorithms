import pytest
from linked_list import LinkedList as ll
from node import Node as nd

@pytest.fixture
def empty_ll():
    return ll()


@pytest.fixture
def small_ll():
    return ll([1, 2])




def test_insert_first_node(empty_ll):
    """test insert node """
    assert empty_ll.head is None
    empty_ll.insert(2)
    assert empty_ll.head.val == 2

def test_node_class():
    """test for node class"""
    assert nd('3').val == '3'

def test_node_class_next():
    """test for next element"""
    assert nd(0,4)._next == 4

def test_node_without_next():
    """test when points to the none"""
    assert nd(3)._next == None

def test_ll_len():
    """test inreract with len"""
    assert len(ll([1,2])) == 2

def test_str_repr_of_ll(small_ll):
    """test small items in array"""
    assert small_ll.head.val == 2
    assert len(small_ll) == 2

def test_small_array_find(small_ll):
    """item in ll"""
    assert small_ll.find(1) == True

def test_small_array_find_not_exist(empty_ll):
    """test item not in ll"""
    assert empty_ll.find(4) == False

def test_find_not_exist(empty_ll):
    """"""
    empty_ll.insert(2)
    assert empty_ll.head.val == 2
    assert len(empty_ll) == 1