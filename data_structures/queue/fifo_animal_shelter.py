from .node import Node


class AnimalShelter:
    
    def __init__(self, iterable=[]):
        """constractor"""
        self.oldest = None
        self.newest = None
        self._len = 0

        for item in iterable:
            self.enqueue(item)
    
    def __repr__(self):
        """print out the front of the q"""
        return 'Queue front: {}'.format(self.oldest.val)

    def __str__(self):
        """ return all items from the q """
        lis = ""
        current = self.oldest
        while current:
            lis += str(current.val) + " "
            current = current.next
        return lis.rstrip()

    def enqueue(self, amiamal):
        """adds animal to the shelter"""
        node = Node(amiamal)
        if self._len == 0:
            self.oldest = self.newest = node
            self._len += 1
            return node
        self.newest.next = node
        self.newest = node
        self._len += 1
        return node

    def dequeue(self, pref=None):
        """remove animal from the"""
        try:
            if pref is None:
                if self._len == 0:
                    return False
                else:
                    self._len -= 1
                    return self.oldest
            """if there is pref"""       
            temp = self.oldest
            while temp.next:
                temp = temp.next
            if temp.val == pref:
                self._len -= 1
                return temp
            else:
                return False
        except IndexError:
            return False
