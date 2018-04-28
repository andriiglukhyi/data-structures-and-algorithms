from linked_list import LinkedList


class HashTable:

    def __init__(self, max_size=1024):
        """init function"""
        self.max_size = max_size
        self.buckets = [None] * self.max_size
        
    def hash_key(self, key):
        """hash function"""
        if type(key) is not str:
            return False

        sum = 0
        for char in key:
            sum += ord(char)
        return sum % len(self.buckets)

    def set(self, key, val):
        """set item to the bucket"""
        if type(key) is not str:
            return False
        
        number = self.hash_key(key)
        if self.buckets[number] is not None:
            if type(self.buckets[number]) == dict:
                # check if item is dict
                ll = LinkedList()
                ll.insert(self.buckets[number])
                ll.insert({key: val})
                self.buckets[number] == ll
                return
            else:
                self.buckets[number].insert({key: val})
                return
        
        self.buckets[number] = {key: val}
    
    def get(self, key):
        """get item from the list"""
        curent_bucket = self.buckets[self.hash_key(key)]
        while curent_bucket.head:
            if curent_bucket.head.val[key]:
                return curent_bucket.head.val[key]
            curent_bucket.head = curent_bucket.head.next
    
    def remove(self, key):
        """remove mode from bucket"""
        # curent_bucket = self.buckets[self.hash_key(key)]

        # curent = curent_bucket.head
        # nxt = curent.next

        # if curent.val[key]:
        #         curent_bucket.head = nxt
        
        # while nxt:
        #     if nxt.val[key]:
        #         curent.next = nxt.next
            

        # self.buckets[self.hash_key(key)] = None
        # return temp
        pass

               
        