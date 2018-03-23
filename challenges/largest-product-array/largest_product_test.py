import largest_product

def test_check_if_array_not_empty():
    """"Check if array is not empty"""
    arr = []
    assert largest_product.largest_product(arr) == 0

def test_check_answer():
    """Check the answer"""
    arr = [3,4,0,5,6,7,8,8,]
    assert largest_product.node_inside(arr, 0) == 64

def test_check_if_each_node_hase_2_elements():
    """"check is nested array hase not rigth num of elements"""
    arr = [[1,1,3,4],[3,1,4,10]]
    assert largest_product.node_to_node(arr[0], arr[1], 0) == True
    