class PriorityQueueBase:
    """Abstract base class for a priority queue."""
    class Item:
        """Lightweight composite to store priority queue items."""
                
        def init(self, k, v):
            self.key = k
            self.value = v
        
        def lt(self, other):  # compare items based on their keys
            return self.key < other.key           
            # concrete method assuming abstract len
    
    def is_empty(self):
        """Return True if the pririty queue is empty"""


class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap."""
#------------------------------ nonpublic behaviors ------------------------------
    def _parent(self, j):
        return (j−1)//2
    
    def _left(self, j):
        return 2*j + 1
    
    def _right(self, j):
        return 2*j + 2
        
    def _has_left(self, j):
        return self._left(j) < len(self._data)
    # index beyond end of list?
    
    def _has_right(self, j):
        return self._right(j) < len(self._data) 
        # index beyond end of list?
    
    def swap(self, i, j):
        """Swap the elements at indices i and j of array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]
    
    def upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self. swap(j, _parent)
    
    def downheap(self, j):
        if self. has_left(j):
            left = self. left(j)
            small_child = left
            if self. has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self.downheap(small child)
    
    def init(self):
        """Create a new empty Priority Queue."""
        self._data = []
    
    def len(self):
        """Return the number of items in the priority queue."""
        return len(self._data)
    
    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self._data.append(self._Item(key, value))
        # upheap newly added position
        self. upheap(len(self._data) − 1)

    def min(self):
        """"Return but do not remove (k,v) tuple with minimum key.Raise Empty exception if empty."""
        if self.is empty():
            raise Empty(Priority queue is empty. )
            item = self. data[0]
return (item. key, item. value)
def remove min(self):
”””Remove and return (k,v) tuple with minimum key.
Raise Empty exception if empty.
”””
if self.is empty( ):
raise Empty( Priority queue is empty. )
# put minimum item at the end
self. swap(0, len(self. data) − 1)
# and remove it from the list;
item = self. data.pop( )
# then fix new root
self. downheap(0)
return (item. key, item. value)