from towers_of_hanoi import towers_of_hanoi as towers


def test_tower():
    """test from odd n"""
    assert towers(3).top.val == 1
    assert len(towers(3)) == 3


def test_tower_even_number():
    """test even number"""
    assert towers(4).top.val == 1
    assert len(towers(4)) == 4


def test_tower_0():
    """test zero us a argument"""
    assert towers(0) is False
    assert towers(-33) is False


def test_big_number():
    """test 100 items in tower"""
    assert towers(20).top.val == 1
    assert len(towers(20)) == 20


def test_other_numbers():
    """test other numbers"""
    stack = towers(7)
    assert stack.top.val == 1
    assert stack.top._next.val == 2
    assert stack.top._next._next.val == 3
    assert stack.top._next._next._next.val == 4 

