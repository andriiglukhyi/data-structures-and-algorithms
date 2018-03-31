from .node import Node


class Queue:
    """class for Queue"""
    def __init__(self, iter=[]):
        self.front = None
        self.back = None
        self._len = 0

        for item in iter:
            self.enqueue(item)
    
    def __len__(self):
        """return len of the corrent object"""
        return self._len
    
    def __str__(self):
        """return items in queue"""
        st = ""
        current = self.front
        while current:
            st += str(current.val) + " "
            current = current._next
        return st.rstrip()
    
    def enqueue(self, val):
        """add new iten to the queue"""
        node = Node(val)
        if len(self) == 0:
            self.front = node
            self.back = node
        else:
            self.back = node
        self._len += 1

    def dequeue(self):
        """remove item from the front"""
        if len(self) == 0:
            return False
        else:
            current = self.front
            self.front = current._next
            self._len -=1
            return current
