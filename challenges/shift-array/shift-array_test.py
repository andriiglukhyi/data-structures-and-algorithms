import shift_array as s


def test_shift_array_if_lenisodd():
    """
    test the case when number of elements is odd number
    """
    array = [0,0,0]
    value = 1
    shift_array(array,value)
    assert array[2] == 1

def test_shift_array_if_leniseven():
    """
    test the case when number of elements is even number
    """
    array = [0,0,0,0]
    value = 1
    shift_array(array,value)
    assert array[2] == 1

def test_shift_array_if_itisempty():
    """
    test the case when array is empty
    """
    array = []
    value = 1
    shift_array
    assert array[0] == 1


