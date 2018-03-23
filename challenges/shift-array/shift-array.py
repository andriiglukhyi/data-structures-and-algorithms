def insert_shift_array(array,value):
    """"""
    if len(array) > 0 and len(array)%2 == 0: 
        midle = len(array)//2
    elif len(array)>0 and len(array)%2 == 1:
        midle = len(array)//2 + 1
    else:
        midle = 0
    new_array = [0]*(len(array)+1)
    for item in range(midle):
        new_array[item] = array[item]
    new_array[midle] = value
    for item in range(midle+1, len(new_array)):
        new_array[item] = array[item-1]
    print(new_array)
    array = new_array
    return array


if __name__ == '__main__':
    insert_shift_array([1,2,3], 4)

     