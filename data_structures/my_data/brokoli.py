class Node():
    """
    create node class for my Brokoli function
    """
    def __init__(self, val):
        """
        init function for node
        """
        if not isinstance(val, int):
            raise TypeError
        self._val = val
        self._buckets = {}

    def __repr__(self):
        """
        repr function for brokoli
        """
        return str(self._val)
    
    def __str__(self):
        """
        strig repr for brokoli
        """
        return str(self._val)
    
    def buckets(self):
        """
        print nodes buckets
        """
        if len(self._buckets) == 0:
            return []
        touples = []
        for key, bucket in self._buckets.items():
            touples.append((key, bucket))
        return touples

class Brokoli:
    """
    create brokoli class
    """
    def __init__(self, iter=None):
        """
        init function for brokoli class
        """
        self._root = None
    
        if iter is not None:
            for item in iter:
                self.insert(item)
    
    def __repr__(self):
        """
        repr function for tree
        """
        if self._root is None:
            return None
        return str(self._root._val)        
    
    def __str__(self):
        """
        string represenation for tree 
        """
        from q import Queue
        st = ""
        if self._root is None:
            return ""
        st += str(self._root._val) + " "
        qu = Queue()
        for item in self._root._buckets.keys():
            qu.enqueue(self._root._buckets[item])
        top = qu.dequeue()
        while top:
            st += str(top._val) + " "
            if len(top._buckets)>0:
                for item in top._buckets.keys():
                    qu.enqueue(top._buckets[item])
            top = qu.dequeue()
        return st.strip()
    
    def insert(self, val):
        """
        insert new element in brokoli
        """
        def _insert(node, val):
            """
            helper function to insert value
            """            
            if val == 0:
                bucket = 0
            else: 
                bucket = node._val % val
            if bucket in node._buckets:
                _insert(node._buckets[bucket], val)
            else:
                node._buckets[bucket] = Node(val)
        if type(val) is not int:
            return False
        if self._root is None:
            self._root = Node(val)
        else:
            _insert(self._root, val)
    
    def pre_order(self, action=None):
        """
        peorder traversal
        """
        def _walk(node=None):
            if node is None:
                return
            action(node.val)
            node_buckets = list(node.buckets.values())
            if len(node.buckets) > 0:
                for node in node_buckets:
                    _walk(node)
        if self._root is None:
            return False
        else:
            _walk(self._root) 
    
    def post_order(self, action=None):
        """
        inorder traversal
        """
        def _walk(node=None):
            if node is None:
                return
            node_buckets = list(node.buckets.values())
            if len(node.buckets) > 0:
                for node in node_buckets:
                    _walk(node)
            action(node.val)
        if self._root is None:
            return False
        else:
            _walk(self._root)

    # def find(self, val):
    #     """
    #     check if exiting value in brokoli
    #     """
    #     def _chek(node.val, val):
    #         """
    #         check if this is curent value
    #         """
    #         if node.val == val:
    #             return True
    #         return 
    #     # use order traversal to traverse brokoli and find value 
    #     self.pre_order(_check)
        


    
data = sorted([4,5,7,5,1,0,8,45,6,3])
nw = Brokoli()

for item in data:
    nw.insert(item)

print(str(nw))
     
