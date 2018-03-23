import largest_product

def check_if_array_not_empty():
    """"Check if array is not empty"""
    arr = []
    assert largest_product.largest_product(arr) == 0

def check_answer():
    """Check the answer"""
    arr = [[1,2],[3,4]]
    assert largest_product.node_inside(arr) == 12

def check_if_each_node_hase_2_elements():
    """"check is nested array hase not rigth num of elements"""
    arr = [[1,1],[3,1]]
    assert largest_product.node_to_node(arr) == 3
    
