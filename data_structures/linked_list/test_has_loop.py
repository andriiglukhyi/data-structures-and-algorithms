import pytest
from linked_list import LinkedList as ll


@pytest.fixture
def empty_ll():
    return ll()


@pytest.fixture
def one_ll():
    return ll([1, 2, 3, 4, 5, 6])


@pytest.fixture
def small_ll():
    return ll([1, 2, 3, 4])


def testt_empty_list_to(small_ll):
    """check if list are empty"""
    assert small_ll.has_loop() is False


def test_has_a_loop(one_ll):
    """check if head is the loop"""
    assert one_ll.has_loop() is False


def test_has_a_loop_(small_ll):
    """check if it will find a loop"""
    current = small_ll.head
    current._next._next._next = small_ll.head
    assert small_ll.has_loop() is True