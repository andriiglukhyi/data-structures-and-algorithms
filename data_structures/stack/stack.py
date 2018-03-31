from .node import Node


class Stack:
    """class for new Stack"""
    def __init__(self, iter=[]):
        self.top = None
        self._len = 0

        for item in iter:
            self.push(item)
    
    def __len__(self):
        """return len of the corrent object"""
        return self._len
    
    def __str__(self):
        """return items in stack"""
        st = ''
        current = self.top
        for _ in range(len(self)):
            print(current.val)
            st += str(current.val)
            current = current._next
        return st.rstrip()
    
    def push(self, val):
        """add item to the stack"""
        self.top = Node(val, self.top)
        self._len += 1
    
    def pop(self):
        """pop one item from top of the stack"""
        if len(self) == 0:
            raise IndexError('no itesm')
        else:
            current = self.top
            self.top = current._next
            self._len -= 1
            return current

    def peek(self):
        if len(self) == 0:
            raise IndexError('stack are empty')
        else:
            return self.top
    
