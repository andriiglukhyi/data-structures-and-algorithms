class Node:
    def __init__(self, val, next=None):
        """new node"""
        self.val = val
        self.next = next

    def __repr__(self):
        return self.val

    def __str__(self):
        return str(self.val)