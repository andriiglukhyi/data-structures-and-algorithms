class Node():
    """
    create node class for my Brokoli function
    """
    def __init__(self, val):
        """
        init function for node
        """
        self.val = val
        self.buckets = [None] * val
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
    
    def __str__(self):
        """
        string represenation for tree 
        """
    
    def insert(self, val):
        """
        insert new element in brokoli
        """
        if self.root is None:
            self.root = Node(val)
        else:
            def _insert(self.root, val):
                bucket = self.root.val % val
                if self.root.buckets[bucket] is None:
                    self.root.buckets[bucket] = Node(val)
                else:
                    _insert(self.root.buckets[bucket], val)
    
    def pre_order(self, action=None):
        """
        peorder traversal
        """
        def _walk(node=None):
            if node is None:
                return
            operation(node.val)
            if node.buckets is not None:
                _walk(node.left)
            if node.right is not None:
                _walk(node.right)
    
    def in_order(self, action=None):
        """
        inorder traversal
        """
    
    def post_order(self):
        """
        postorder traversal
        """
    def find(self, val):
        """
        check if exiting value in brokoli
        """


    
    
     
