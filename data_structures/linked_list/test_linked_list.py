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
    assert nd(0, 4)._next == 4


def test_node_without_next():
    """test when points to the none"""
    assert nd(3)._next is None


def test_ll_len():
    """test inreract with len"""
    assert len(ll([1, 2])) == 2


def test_str_repr_of_ll(small_ll):
    """test small items in array"""
    assert small_ll.head.val == 2
    assert len(small_ll) == 2


def test_small_array_find(small_ll):
    """item in ll"""
    assert small_ll.find(1) is True


def test_small_array_find_not_exist(empty_ll):
    """test item not in ll"""
    assert empty_ll.find(4) is False


def test_find_not_exist(empty_ll):
    """find node which dont exist"""
    empty_ll.insert(2)
    assert empty_ll.head.val == 2
    assert len(empty_ll) == 1


def test_append_method(small_ll):
    """append new node to the end"""
    small_ll.append(4)
    assert small_ll.__str__ == '[124]'


def test_append_method_a_couple_elements(small_ll):
    """append couple elements"""
    small_ll.append(1)
    small_ll.append(5)
    assert len(small_ll) == 4


def test_insertBefore(small_ll):
    """insert new node before rigth one"""
    small_ll.insert_before(2, 10)
    assert small_ll == '1102'


def test_insertBefore_change_head(small_ll):
    """insert new node at the head and change pointer"""
    small_ll.insert_before(1, 5)
    assert small_ll.head == 5


def test_insertAfter(small_ll):
    """insert new node after correct value"""
    small_ll.insert_after(2, 4)
    assert small_ll == '124'


def test_insertAfter_(small_ll):
    """check if last is pointed to the None"""
    small_ll.insert_after(2, 4)
    small_ll.insert_after(4, 6)
    assert small_ll.__str__[-1] == '6'


def test_kth_from_end(small_ll):
    """test element at 0 position"""
    assert small_ll.ll_kth_from_end(0).val == 2


def test_kth_from_end_out_of_range(small_ll):
    """test if list out of range"""
    assert small_ll.ll_kth_from_end(10) is False


def test_kth_from_end_less_then_0(small_ll):
    """test if value in appropeiate"""
    assert small_ll.ll_kth_from_end(-5) is False