def largest_product(arr):
    """function will take array and return number"""
    largest = 0
    if len(arr) == 0:
        print(largest)
        return largest
    elif len(arr) == 1:
        largest = node_inside(arr[0], largest)
        print(largest)
    else:
        for item in range(len(arr)-1):
            largest = node_inside(arr[item],largest)
            largest = node_to_node(arr[item], arr[item+1], largest)
    
        largest = node_inside(arr[len(arr)-1], largest)
    print(largest)
    return largest


def node_inside(sub_arr, largest):
    """item in one node"""
    if len(sub_arr) == 1:
        largest = sub_arr[0]
        return largest
    else:
        for item in range(len(sub_arr)-1):
            if sub_arr[item]*sub_arr[item+1] > largest:
                largest = sub_arr[item]*sub_arr[item+1]
        return largest


def node_to_node(node1, node2, largest):
    """campare two items"""
    if len(node1) == len(node2):
        for a in range(len(node1)):
            if node1[a]*node2[a] > largest:
                largest = node1[a]*node2[a]
    return largest
