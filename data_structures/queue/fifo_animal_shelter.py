from .node import Node


class Animal:
    pass


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class AnimalShelter:
    
    def __init__(self, iterable=[]):
        """constractor"""
        self.oldest = None
        self.newest = None
        self._len = 0

        for item in iterable:
            self.enqueue(item)

    def __str__(self):
        """ return all items from the q """
        lis = []
        current = self.oldest
        while current:
            lis.append(current)
            current = current.next
        return lis

    def enqueue(self, animal):
        """adds animal to the shelter"""
        if self._len == 0:
            self.oldest = self.newest = animal
            self._len += 1
            return self.oldest
        self.newest.next = animal
        self.newest = animal
        self._len += 1
        return self.newest

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
                if isinstance(temp, pref):
                    self._len -= 1
                return temp
            else:
                return False
        except IndexError:
            return False

