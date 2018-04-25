class Node:
    """node class for stack"""
    def __init__(self, val, next=None):
        """new node"""
        self.val = val
        self._next = next
        
    def __repr__(self):
        """repr of node"""
        return self.val

    def ___str___(self):
        """string repr of node"""
        return str(self.val)