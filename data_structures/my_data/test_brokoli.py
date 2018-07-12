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
        # ans = ""
        # def add_string(node.val):
        #     nonlocal ans
        #     """
        #     fucntion to add values to string
        #     """
        #     ans += str(node.val)
        
        # if self.root is None:
        #     return ans
        # else:
        #     self.pre_order(self.root, add_string)
        pass

            
    
    def __str__(self):
        """
        string represenation for tree 
        """
    
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
            bucket = self.root.val % val
            if bucket not in self.root.buckets:
                self.root.buckets[bucket] = Node(val)
            else:
                self.insert(self.root.buckets[bucket], val)
    
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
    
     
