def left_join(map1, map2):
    number = 0
    for item in map2.buckets:
        if type(item) == dict:
            number += 1
    print(number)

    if number > 0:  
        end = []
        for item in map1.buckets:
            if type(item) == dict:
                temp = []
                if type(item) == dict:
                    temp.append(list(item.keys())[0])
                    temp.append(list(item.values())[0])
                    num = map2.hash_key(list(item.keys())[0])
                    if type(map2.buckets[num]) == dict:
                        temp.append(list(map2.buckets[num].values())[0])
                    else:
                        temp.append(None)
                end.append(temp)
        return end
    else:
        return [x for x in map1.buckets if type(x) == dict] 

