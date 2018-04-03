from queue_with_stacks import Queue as q
import pytest


@pytest.fixture
def empty_q():
    return q()


@pytest.fixture
def small_q():
    return q([1, 2, 4, 5])


def test_constractor(empty_q):
    """test cinstractor function"""
    assert empty_q._len == 0


def test_enquueue(empty_q, small_q):
    """test enqueu on small and empty queue"""
    assert empty_q.enqueue(1) == empty_q.stack1
    assert empty_q.enqueue(10) == empty_q.stack1


def test_enqueue_val(empty_q, small_q):
    """test dequeu method"""
    empty_q.enqueue(5)
    small_q.enqueue(25)
    assert empty_q.stack1.top.val == 5
    assert small_q.stack1.top.val == 25


def test_dequeu_(small_q):
    """test dequeue from small q"""
    assert small_q.dequeue() == 2


def test_enqueue_and_dequeue(empty_q):
    """test empty q"""
    empty_q.enqueue(4)
    assert empty_q.dequeue() == 4


