from node import Node


class LinkedList:
    """class for new linked lists"""
    def __init__(self, iter=[]):
        self.head = None
        self._len = 0

        for item in iter:
            self.head = self.insert(item)

    def __len__(self):
        """return len of the corrent object"""
        return self._len

    def __str__(self):
        """return all items from the LL"""
        lis = ''
        current = self.head
        for _ in range(self._len+1):
            lis += str(current.val) + " "
            current = current._next
        return lis

    def insert(self, val):
        """add item to the LL"""
        self.head = Node(val, self.head)
        self._len += 1
    
    def find(self, val):
        """search for element and return True or false"""
        if self.head is None:
            return False
        elif self.head.val == val:
            return True
        else:
            current = self.head
            while current is not None:
                if current.val == val:
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
    
    def ll_kth_from_end(self, k):
        """ find node (k) from end """
        x = self._len - (k-1)
        node = self.head
        counter = 0
        while node:
            if counter == x:
                return node
            counter += 1
            node = node._next
        raise IndexError('Requested node outside link list length')
    
    def has_loop(self):
        """mrthod will cj=heck for the loop inside LL"""
        if self.head is None:
            return False
        if self.head._next is self.head:
            return True
        slow = self.head
        fast = self.head
        while fast is not None:
            slow = slow._next
            fast = fast._next._next
            if slow is fast:
                return True
            return False


def merge_lists(list1, list2):
    """merge two linked list"""
    if len(list1) == 0:
        return list2.head
    elif len(list2) == 0:
        return list1.head
    else:
        current_1 = list1.head
        current_2 = list2.head
        current_3 = current_2._next
        while current_1 and current_2:
            current_2 = current_3
            current_1._next, current_2._next = current_2, current_1._next
            current_1 = current_1._next
        return list1.head


            
     

    
    





