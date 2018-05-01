from linked_list import LinkedList


class HashTable:

    def __init__(self, max_size=1024):
        """init function"""
        self.max_size = max_size
        self.buckets = [None] * self.max_size
        
    def hash_key(self, key):
        """hash function"""
        key = str(key)

        sum = 0
        for char in key:
            sum += ord(char)
        return sum % len(self.buckets)

    def set(self, key, val=None):
        """set item to the bucket"""
        if val is None:
            val = key
        key = str(key)   
        number = self.hash_key(key)
        if self.buckets[number] is not None:
            if type(self.buckets[number]) == dict:
                # check if item is dict
                ll = LinkedList()
                ll.insert(self.buckets[number])
                ll.insert({key: val})
                print(ll.head)
                self.buckets[number] = ll
                print(self.buckets[number].head.val)
            else:
                self.buckets[number].insert({key: val})
        
        else:
            self.buckets[number] = {key: val}
    
    def get(self, key):
        """get item from the list"""
        if type(key) is not str:
            return False
        number = self.hash_key(key)
        if self.buckets[number] is not None:
            curent_bucket = self.buckets[number]
            if type(curent_bucket) != dict:
                curent = curent_bucket.head
                while curent:
                    if key in curent.val:
                        return curent.val[key]
                    curent = curent._next
                    return False  # if key not in the bucket

            else:
                return self.buckets[number][key]
        else:
            return False
                        
    def remove(self, key):
        """remove mode from bucket"""
        if type(key) is not str:
            return False
        number = self.hash_key(key)
        if self.buckets[number] is not None:
            curent_bucket = self.buckets[number]
            curent = curent_bucket.head
            if curent._next:
                if key in curent.val:
                    temp = curent.val[key]
                    curent_bucket.head = curent_bucket.head._next
                    return
                while curent._next:
                    nxt = curent._next
                    if nxt.val[key]:
                        temp = nxt.val[key]
                        curent = nxt._next
                        return temp
                return False
            else:
                temp = curent.val[key]
                self.buckets.remove(self.buckets[number])
                return temp
        else:
            return False