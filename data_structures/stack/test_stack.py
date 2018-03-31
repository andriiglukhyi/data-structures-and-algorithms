import pytest

from .stack import Stack as st


@pytest.fixture
def empty_st():
    return st()


@pytest.fixture
def small_st():
    return st([1, 2, 4, 5])


def test_empty_empty_st(empty_st):
    assert empty_st.top is None
    assert len(empty_st) == 0


def test_constractor():
    s = st([1, 2])
    assert len(s) == 2
    assert s.top.val == 2


def test_empty_empty_add(empty_st):
    empty_st.push(2)
    assert empty_st.top.val == 2
    assert len(empty_st) == 1


def test_small_len(small_st, empty_st):
    assert len(small_st) == 4
    assert len(empty_st) == 0


def test_small_str(empty_st):
    assert str(empty_st) == ''


def test_small_str_(small_st):
    assert str(small_st) == '5421'


def test_small_pop(small_st):
    current = small_st.top
    assert small_st.pop() is current
    assert len(small_st) == 3


def test_small_push(small_st):
    small_st.push(2)
    small_st.push(4)
    assert len(small_st)


def test_pus(empty_st):
    empty_st.push(1)
    assert empty_st.top.val == 1 
    assert len(empty_st) == 1


def test_peek(small_st, empty_st):
    assert small_st.peek() == small_st.top
    assert len(small_st) == 4