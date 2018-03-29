import pytest
from linked_list import LinkedList as ll
from linked_list import merge_lists as merge


@pytest.fixture
def ll_one():
    return ll([1, 2, 3])

@pytest.fixture
def ll_two():
    return ll([6, 7, 8])

@pytest.fixture
def small_():
    return ll([10, 11])

@pytest.fixture
def empty_():
    return ll([])




def test_merge_two_equal_list(ll_one,ll_two):
    """test two equal lists"""
    assert merge(ll_one, ll_two) ==  ll_one.head

def test_merge_with_empty(ll_one, empty_):
    """test if one list are empty"""
    assert merge(ll_one,empty_) == ll_one.head

def test_merge_second_empty(empty_, ll_two):
    """checko if second argument is empty list"""
    assert merge(empty_, ll_two) == ll_two.head

def test_merge_first_smaller(ll_one, small_):
    """check if second list are smaller"""
    assert merge(ll_one, small_) == ll_one.head
 

