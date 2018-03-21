def binnarySearch(arr, val):
    counter = 0
    if len(arr) = 0:
        print('array c\'ant be empty')
        return -1
    elif type(val) != int:
        print('value should be a number')
        return -1
    else:
        len(arr) > 0 and type(val) == int:
            for item in arr:
                counter +=1
                if item == val:
                    print(counter)
                    return counter
                else:
                    print('inncorrect')
                    return -1

if __name__ == '__main__':
    binnarySearch([1,2,3,4], 4)