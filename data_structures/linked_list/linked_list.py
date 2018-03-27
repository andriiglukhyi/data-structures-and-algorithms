from node import Node

class LinkedList:
    """class for new linked lists"""
    def __init__(self, iter = []):
        self.head = None
        self._len = 0 

        for item in iter:
            self.head = Node(item, self.head)
            self._len += 1

    

    def __len__(self):
        """return len of the corrent object"""
        return self._len
    
    
    def __str__(self):
        """return all items from the LL"""
        lis = []
        current = self.head
        for _ in range(self._len+1):
            lis.append(current)
            current = current._next
        return str(lis)

    
    def insert(self, val):
        """add item to the LL"""
        self.head = Node(val, self.head)
        self._len += 1
    

    def find(self, val):
        """search for element and return True or false"""
        if self.head == None:
            return False
        elif self.head == val:
            return True
        else:
            current = self.head
            nxt = current._next
            if nxt.val == val:
                return True
            else:
                while nxt.val != val and nxt is not None :
                    current = nxt
                    nxt = current._next
                if nxt.val == val:
                    return True
                return False
    
    def append(self, value):
        """append value at the end of the list"""
        current = self.head
        if current:
            while current._next:
                current = current._next
            current._next = Node(value)
        else:
            self.head = Node(value)
        return self.__str__

    
    def insert_before(self, value, newval):
        """insert new node before correct"""
        current = self.head
        if current:
            while current._next.val != value:
                current = current._next
            current._next = Node(newval, current._next)
        else:
            self.head = Node(value)
        return self.__str__
            

    
    def insert_after(self, value, newval):
        """insert new node after correct"""
        current = self.head
        if current:
            while current.val != value:
                current = current._next
            current._next = Node(newval, current._next)
            return True
        else:
            self.head = Node(value)
            return True
        return False  
    
    def ll_kth_from_end(self, value):
        current = self.head
        if len(self) - 1 < value  or value < 0:
            print('out of range')
            return False
        else:
            for item in range(value - 1):
                current = current._next
        return current




