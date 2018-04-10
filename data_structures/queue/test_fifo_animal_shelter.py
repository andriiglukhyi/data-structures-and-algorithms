import pytest

from .fifo_animal_shelter import AnimalShelter, Cat, Dog


@pytest.fixture
def empty_dog_q():
    return AnimalShelter()


@pytest.fixture
def dog_q():
    return AnimalShelter([Dog(), Dog(), Dog(), Dog()])


@pytest.fixture
def cat_q():
    return AnimalShelter([Cat(), Cat(), Cat(), Cat()])


@pytest.fixture
def mix_q():
    return AnimalShelter([Cat(), Dog(), Cat(), Cat(), Cat(), Cat(), Cat(), Dog()])


def test_contsractor(empty_dog_q):
    """test constarctor"""
    assert empty_dog_q is None
    assert empty_dog_q is None


def test_enquu(dog_q):
    """test enquueu"""
    dog_q.enqueue(Cat())
    assert dog_q.newest == Cat()
    assert dog_q._len == 6


# def test_empty_dog_q(empty_dog_q):
#     """test dequeue"""
#     empty_dog_q.enqueue('cat')
#     assert empty_dog_q._len == 1
#     assert empty_dog_q.newest.val and empty_dog_q.oldest.val == 'cat'


# def test_dequeu(empty_dog_q):
#     """test dequeu from the empty q"""
#     assert empty_dog_q.dequeue() is False


# def test_dequeu_not_in_Queue(cat_q, dog_q):
#     """test dequueu if item not in """
#     assert cat_q.dequeue('dog') is False
#     assert dog_q.dequeue('cat') is False


# def test_mix_q_dog(mix_q):
#     mix_q.dequeue('dog')
#     assert mix_q._len == 8
#     mix_q.dequeue()
#     assert mix_q._len == 7


