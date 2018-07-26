import pytest
from brokoli import Node, Brokoli

@pytest.fixture
def simple_node():
    """
    Test Node class
    """
    return Node(5)


@pytest.fixture
def empty_brokoli():
    """
    Empty
    """
    return Brokoli()


@pytest.fixture
def small_brokoli():
    """
    Small brokoli
    """
    return Brokoli([11,2,0,1,5,4])

@pytest.fixture
def big_brokoli():
    """
    Big brokoli
    """
    return Brokoli([1,9,10,11,5,4,7,8,2,8,5,5,3,8,9,3,4,5,6,5,1,1,0])


def test_node(simple_node):
    """
    Test node init
    """
    assert simple_node._val == 5
    assert str(simple_node) == "5"
    assert len(simple_node.buckets()) == 0

def test_node_tring():
    """
    Test node class
    """
    with pytest.raises(TypeError):
        # empty string
        Node("")
        # string
        Node("string")
        # Boolena
        Node(True)
        # class
        Node(Node("1"))

def test_empty_brokoli(empty_brokoli):
    """
    Test empty brokoli
    """
    assert empty_brokoli._root is None
    assert str(empty_brokoli) == ""
    empty_brokoli.insert(5)
    assert empty_brokoli._root._val == 5
    assert str(empty_brokoli) == "5"
    assert empty_brokoli.insert("") is False
    assert repr(empty_brokoli) == "5"

# def test_

