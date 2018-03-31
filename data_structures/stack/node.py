class Node:
    def __init__(self, val, next=None):
        self.val = val
        self._next = None
    
    def __repr__(self):
        return self.val