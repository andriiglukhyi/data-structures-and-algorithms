from quicksort import quicksort as qs


def test_small_array():
    """test array with length les then 2"""
    assert qs([1]) == [1]
    assert qs([]) == []


def test_midium_array():
    """test midium size array"""
    arr = [2, 4, 1, 3, 40, 34, 11]
    assert qs(arr) == sorted(arr)


def test_big_array():
    """test big array"""
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3]
    assert qs(arr) == sorted(arr)


def test_mixed_array():
    arr = [7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1]
    assert qs(arr) == sorted(arr)