import pytest

from .fifo_animal_shelter import AnimalShelter as animal



@pytest.fixture
def empty_dog_q():
    return animal()


@pytest.fixture
def dog_q():
    return animal(['dog', 'dog', 'dog', 'dog', 'dog'])


@pytest.fixture
def cat_q():
    return animal(['cat', 'cat', 'cat', 'cat', 'cat', 'cat'])


@pytest.fixture
def mix_q():
    return animal(['cat', 'dog', 'cat', 'dog', 'cat', 'cat', 'dog', 'cat', 'dog'])


def test_contsractor():
    """test constarctor"""
    ne = animal()
    assert ne.newest is None
    assert ne.oldest is None


def test_enquu(dog_q):
    """test enquueu"""
    dog_q.enqueue('cat')
    assert dog_q.newest.val == 'cat'
    assert dog_q._len == 6


def test_empty_dog_q(empty_dog_q):
    """test dequeue"""
    empty_dog_q.enqueue('cat')
    assert empty_dog_q._len == 1
    assert empty_dog_q.newest.val and empty_dog_q.oldest.val == 'cat'


def test_dequeu(empty_dog_q):
    """test dequeu from the empty q"""
    assert empty_dog_q.dequeue() is False


def test_dequeu_not_in_Queue(cat_q, dog_q):
    """test dequueu if item not in """
    assert cat_q.dequeue('dog') is False
    assert dog_q.dequeue('cat') is False


def test_mix_q_dog(mix_q):
    mix_q.dequeue('dog')
    assert mix_q._len == 8
    mix_q.dequeue()
    assert mix_q._len == 7


