class Node:
    def __init__(self, val, next=None):
        """new node"""
        self.val = val
        self._next = next
        
    def __repr__(self):
        return self.val