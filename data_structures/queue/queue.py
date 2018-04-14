from .node import Node


class Queue:
    def __init__(self, iterable=[]):
        self.back = None
        self.front = None
        self._len = 0

        for item in iterable:
            self.enqueue(item)

    def __repr__(self):
        """print out the front of the q"""
        return self.front.val

    def __str__(self):
        """ return all items from the LL """
        lis = ""
        current = self.front
        while current:
            lis += str(current.val) + " "
            current = current.next
        return lis.rstrip()

    def enqueue(self, val):
        node = Node(val)
        if self._len == 0:
            self.front = self.back = node
            self._len += 1
            return node
        self.back.next = node
        self.back = node
        self._len += 1
        return node

    def dequeue(self):
        if self._len == 0:
            return False
        temp = self.front
        self.front = temp.next
        self._len -= 1
        return temp