from stack import Stack as stack
# from .node import Node as Node


class Queue:
    """class for Queue"""
    def __init__(self, iter=[]):
        self.stack1 = stack()
        self.stack2 = stack()
        self._len = 0

        for item in iter:
            self.enqueue(item)
    
    def enqueue(self, val):
        """add new iten to the queue"""
        if val:
            self.stack1.push(val)
            self._len += 1
            return self.stack1
        
        return False

    def dequeue(self):
        """remove item from the front"""
        if self._len == 0:
            return False
        else:
            for _ in range(self._len - 2):
                self.stack2.push(self.stack1.pop())
            last = self.stack1.pop()
            for _ in range(self._len - 2):
                self.stack1.push(self.stack2.pop())
            self._len -= 1
            return last

