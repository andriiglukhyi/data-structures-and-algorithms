from towers_of_hanoi import towers_of_hanoi as towers

def test_tower():
    """test from odd n"""
    print(str(towers(3)))
    assert towers(4).top.val == 4
