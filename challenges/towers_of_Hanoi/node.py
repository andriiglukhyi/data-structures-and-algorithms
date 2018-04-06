class Node:
    def __init__(self, val, next=None):
        self.val = val
        # import pdb; pdb.set_trace()
        self._next = next
        
    def __repr__(self):
        return str(self.val)