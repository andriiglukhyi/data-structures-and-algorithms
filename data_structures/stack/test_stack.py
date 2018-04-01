import pytest

from .stack import Stack as st


@pytest.fixture
def empty_st():
    return st()


@pytest.fixture
def small_st():
    return st([1, 2, 4, 5])


def test_empty_empty_st(empty_st):
    """check if top of the empty stack is none"""
    assert empty_st.top is None
    assert len(empty_st) == 0


def test_constractor():
    """check len method of non empty stack"""
    s = st([1, 2])
    assert len(s) == 2
    assert s.top.val == 2


def test_empty_empty_add(empty_st):
    """test push method"""
    empty_st.push(2)
    assert empty_st.top.val == 2
    assert len(empty_st) == 1


def test_small_len(small_st, empty_st):
    """test len prebuid list"""
    assert len(small_st) == 4
    assert len(empty_st) == 0


def test_small_str(empty_st):
    """test string method of stack"""
    assert str(empty_st) == ""


def test_small_str_(small_st):
    """test string repr of non rmpty list"""
    assert str(small_st) == str([5, 4, 2, 1])


def test_small_pop(small_st):
    """test pop method"""
    current = small_st.top
    assert small_st.pop() is current
    assert len(small_st) == 3


def test_small_push(small_st):
    """test push method"""
    small_st.push(2)
    small_st.push(4)
    assert len(small_st)


def test_push(empty_st):
    """test push on non empty"""
    empty_st.push(1)
    assert empty_st.top.val == 1 
    assert len(empty_st) == 1


def test_peek(small_st, empty_st):
    """test peek method"""
    assert small_st.peek() == small_st.top
    assert len(small_st) == 4


