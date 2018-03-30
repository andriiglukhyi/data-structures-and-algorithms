import shift_array as s


def test_shift_array_if_lenisodd():
    """test the case when number of elements is odd number"""
    array = [0, 0, 0]
    value = 1
    assert s.insert_shift_array(array, value) == [0, 0, 1, 0]


def test_shift_array_if_leniseven():
    """test the case when number of elements is even number"""
    array = [0, 0, 0, 0]
    value = 1
    assert s.insert_shift_array(array, value) == [0, 0, 1, 0, 0]


def test_shift_array_if_itisempty():
    """test the case when array is empty"""
    array = []
    value = 1
    assert s.insert_shift_array(array, value) == [1]


def test_shift_array_value_not_int():
    """test if value is not int"""
    array = []
    value = 'a'
    assert s.insert_shift_array(array, value) is False


def test_if_first_par_isnt_array():
    """check false parameters"""
    arr = 1
    val = 1
    assert s.insert_shift_array(arr, val) is False



