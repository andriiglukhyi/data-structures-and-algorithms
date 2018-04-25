class Node:
    def __init__(self, val, next=None):
        """new node"""
        self.val = val
        self.next = next

    def __repr__(self):
        """representation of node val"""
        return self.val

    def __str__(self):
        """string representation"""
        return str(self.val)