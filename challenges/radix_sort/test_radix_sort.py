from radix_sort import radix_sort


def test_empty_array():
    """
    """
    arr = []
    assert radix_sort(arr) == []


def test_small_array():
    """
    test small array
    """
    arr = [4, 2, 5, 10, 4]
    assert radix_sort(arr) == sorted(arr)


def test_big_array():
    """
    test big array
    """
    arr = [1000, 100, 10, 0]
    assert radix_sort(arr) == sorted(arr)