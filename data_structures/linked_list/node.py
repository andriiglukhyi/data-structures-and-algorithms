class Node:
    def __init__(self, val, next=None):
        """init function"""
        self.val = val
        self._next = next

    def __str__(self):
        """str representation"""
        return str(\self.val)