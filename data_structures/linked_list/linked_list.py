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
        print(current.val)
        while current._next:
            lis += str(current.val) + ' '
            current = current._next
        return lis

    def insert(self, val):
        """add item to the LL"""
        node = Node(val, self.head)
        # self.head = Node(val, self.head)
        self.head = node
        self._len += 1
        print(self.head.val)
        return self.head

    
    def find(self, val):
        """search for element and return True or false"""
        if self.head is None:
            return False
        elif self.head == val:
            return True
        else:
            current = self.head
        while current:
            if val == current:
                return True
            current = current._next
        return False

    def append(self, value):
        """append value at the end of the list"""
        current = self.head
        while current._next:
            current = current._next
            # print(current.val)
        current._next = Node(value)
        print(current.val)
        # print(current._next.val)

        self._len += 1
    
    def insert_before(self, value, newval):
        """insert new node before correct"""
        current = self.head
        if current:
            while current._next != value:
                current = current._next
            current._next = Node(newval, current._next)
            self._len += 1
        else:
            self.head = Node(value)
            self._len += 1
        return self.__str__
    
    def insert_after(self, value, newval):
        """insert new node after correct"""
        current = self.head
        if current:
            while current.val != value:
                current = current._next
            current._next = Node(newval, current._next)
            self._len += 1
            return True
        else:
            self.head = Node(value)
            self._len += 1
            return True
        return self.__str__
    
    def ll_kth_from_end(self, k):
        """ find node (k) from end """
        if k < 0 or self._len - k < 0:
            return False
        x = self._len - (k-1)
        node = self.head
        counter = 0
        while node:
            if counter == x:
                return node
            counter += 1
            node = node._next
            return node
    
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


            
     

    
    





