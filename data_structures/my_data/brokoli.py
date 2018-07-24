class Node():
    """
    create node class for my Brokoli function
    """
    def __init__(self, val):
        """
        init function for node
        """
        self.val = val
        self.buckets = {}
    def __repr__(self):
        """repr function for brokoli"""
        return str(self.val)
    
    def __str__(self):
        """strig repr for brokoli"""
        return str(self.val)
class Brokoli:
    """
    create brokoli class
    """
    def __init__(self):
        """
        init function for brokoli class
        """
        self.root = None
    
    def __repr__(self):
        """
        repr function for tree
        """
        pass

            
    
    def __str__(self):
        """
        string represenation for tree 
        """
        from q import Queue
        st = ""
        if self.root is None:
            return False
        st += str(self.root.val) + " "
        qu = Queue()
        for item in self.root.buckets.keys():
            print(self.root.buckets.keys())
            qu.enqueue(self.root.buckets[item])
        top = qu.dequeue()
        while top:
            st += str(top.val) + " "
            if len(top.val.buckets)>0:
                for item in top.val.buckets.keys():
                    qu.enqueue(top.val.buckets[item])
            top = qu.dequeue()
        return st
    
    def insert(self, val):
        """
        insert new element in brokoli
        """
        def _insert(node, val):
            """
            helper function to insert value
            """
            
        if self.root is None:
            self.root = Node(val)
        else:
            if val == 0:
                bucket = 0
            else: 
                bucket = self.root.val % val
            if bucket in self.root.buckets:
                _insert(self.root.buckets[bucket], val)
            else:
                self.root.buckets[bucket] = Node(val)
    
    def pre_order(self, action=None):
        """
        peorder traversal
        """
        def _walk(node=None):
            if node is None:
                return
            operation(node.val)
            node_buckets = list(node.buckets.values())
            if len(node.buckets) > 0:
                for node in node_buckets:
                    _walk(node)
        if self.root is None:
            return False
        else:
            _walk(self.root) 
    
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
            operation(node.val)
        if self.root is None:
            return False
        else:
            _walk(self.root)

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
        


    
data = [4,5,7,5,1,0,8,45,6,3]
nw = Brokoli()

for item in data:
    nw.insert(item)
    
     
