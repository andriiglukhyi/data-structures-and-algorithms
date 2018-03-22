import binary_search

def test_array_if_empty():
    """
    Test shpuld check case when array are empty
    """
    arr = []
    val = 10
    assert binary_search.binary_search(arr,val) == -1 

def test_val_in_array():
    """
    Test if current value in array
    """
    arr = [1,2,3,4,5]
    val = 6
    assert binary_search.binary_search(arr,val) == -1

