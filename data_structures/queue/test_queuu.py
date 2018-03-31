import pytest

from .queue import Queue as q


@pytest.fixture
def empty_q():
    return q()


@pytest.fixture
def small_q():
    return q([1, 2, 4, 5])


def test_empty_empty_q(empty_q):
    assert empty_q.front is None
    assert empty_q.back is None
    assert len(empty_q) == 0


def test_constractor(empty_q):
    empty_q.enqueue(1)
    empty_q.enqueue(2)
    assert len(empty_q) == 2
    assert empty_q.front.val == 1
    assert empty_q.back.val == 2


def test_empty_empty_add(empty_q):
    empty_q.enqueue(2)
    assert empty_q.front.val == 2
    assert len(empty_q) == 1
    assert empty_q.back.val == 2


def test_small_len(small_q, empty_q):
    assert len(small_q) == 4
    assert len(empty_q) == 0


def test_small_str(small_q):
    assert str(small_q) == '5 4 2 1'


def test_small_enquue(small_q):
    small_q.enqueue(3)
    assert small_q.front.val == 1
    assert small_q.back.val == 3


def test_enquueu_(small_q):
    small_q.enqueue(7)
    assert small_q.back.val == 7 


def test_dequue(small_q):
    current = small_q.front
    assert small_q.dequeue() is current


def test_dequue_len(small_q):
    small_q.dequeue()
    assert len(small_q) == 3


def test_empty_dequeue(empty_q):
    assert empty_q.dequeue() is False