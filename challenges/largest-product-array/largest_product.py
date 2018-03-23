def largest_product(arr):
    largest = 0
    mainlen = len(arr)
    if len(arr) == 0:
        print(largest)
        return largest
    elif len(arr) == 1:
        largest = arr[0]*arr[1] 
        print(largest)
        return largest
    else:
        for node in range(mainlen-1):
            print(arr[node])
            # if len(arr[node]) == 2 and len(arr[node+1]) ==2:
            #     if arr[node][0]*arr[node][1] > largest:
            #         largest = arr[node][0]*arr[node][1]
            #     elif arr[node][0]*arr[node+1][0] > largest:
            #         largest = arr[node][0]*arr[node+1][0]
            #     else:
            #         largest = arr[node][1]*arr[node+1][1]
            else:
                print("not enougth items")
                return -1
        if arr[len(arr)][0]*arr[len(arr)][1]:
            largest = arr[len(arr)][0]*arr[len(arr)][1]
def node_inside(sub_arr, largest):
    for item in range(len(arr)-1):
        if syb_arr[item]*sub_arr[item+1] > largest:
            largest = syb_arr[item]*sub_arr[item+1]
        return largest 
def node_to_node(len, node1,node2,largest):
    for item in range(len):
        if len(node1) == len(node2):
            for item in range(len(node1)):
                if node1[item]*node2[item]






if __name__ == '__main__':
    largest_product([ [ 1, 2 ], [ 3, 4 ], [ 5, 6 ], [ 7, 8 ] ])