from multi_bracket_validation import multi_bracket_validation as multi


def test__empty_input():
    """test if input is not a string"""
    assert multi('') is True


def test_match_input():
    """test correct input"""
    assert multi('[[][]]') is True


def test_not_match_input():
    """test not match input"""
    assert multi('{{[}}') is False


def test_wrong_input():
    """test input is not a string"""
    assert multi([1, 2, 3, 4]) is False


def test_new():
    assert multi('[[[abc]]') is False