import binary_search


def test_array_if_empty():
    """Test shpuld check case when array are empty"""
    arr = []
    val = 10
    assert binary_search.binary_search(arr, val) is False


def test_val_in_array():
    """Test if current value not in array"""
    arr = [1, 2, 3, 4, 5]
    val = 0
    assert binary_search.binary_search(arr, val) is False


def test_val_in_array_not_in_array():
    """Test if current value in array"""
    arr = [1, 2, 3, 6, 7, 9, 11]
    val = 10
    assert binary_search.binary_search(arr, val) is False