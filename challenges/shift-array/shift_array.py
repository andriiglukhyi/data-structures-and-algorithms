def insert_shift_array(array, value):
    """algoritm should add element in array and shit tht array to the rigth"""
    if type(value) != int or type(array) != list:
        return False
    elif len(array) == 0:
        array.append(value)
        return array
    else:
        if len(array) > 0 and len(array) % 2 == 0: 
            midle = len(array)//2
        elif len(array) > 0 and len(array) % 2 == 1:
            midle = len(array)//2 + 1
        else:
            midle = 0
        new_array = [0]*(len(array)+1)
        for item in range(midle):
            new_array[item] = array[item]
        new_array[midle] = value
        for item in range(midle+1, len(new_array)):
            new_array[item] = array[item-1]
        array = new_array
        print(array)
    return array
    