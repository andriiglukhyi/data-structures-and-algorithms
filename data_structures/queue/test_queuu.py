import pytest

from .queue import Queue as q


@pytest.fixture
def empty_q():
    return q()


@pytest.fixture
def small_q():
    return q([1, 2, 4, 5])


def test_empty_empty_q(empty_q):
    """test empty queue"""
    assert empty_q.front is None
    assert empty_q.back is None
    assert empty_q._len == 0


def test_constractor(empty_q):
    """test multiply enqueue"""
    empty_q.enqueue(1)
    empty_q.enqueue(2)
    assert empty_q._len == 2
    assert empty_q.front.val == 1
    assert empty_q.back.val == 2


def test_empty_empty_add(empty_q):
    """test enqueue with empty"""
    empty_q.enqueue(2)
    assert empty_q.front.val == 2
    assert empty_q._len == 1
    assert empty_q.back.val == 2


def test_small_len(small_q, empty_q):
    """test len method """
    assert small_q._len == 4
    assert empty_q._len == 0


def test_small_str(small_q):
    """test str repr"""
    # import pdb; pdb.set_trace()
    assert str(small_q) == '1 2 4 5'


def test_small_enquue(small_q):
    """test front and back"""
    small_q.enqueue(3)
    assert small_q.front.val == 1
    assert small_q.back.val == 3


def test_enquueu_(small_q):
    """test enquuue back  """
    small_q.enqueue(7)
    assert small_q.back.val == 7


def test_dequue(small_q):
    """test dequeue"""
    current = small_q.front
    assert small_q.dequeue() is current


def test_dequue_len(small_q):
    """test dequeue len"""
    small_q.dequeue()
    assert small_q._len == 3


def test_empty_dequeue(empty_q):
    """test qdequeu empty queue"""
    assert empty_q.dequeue() is False