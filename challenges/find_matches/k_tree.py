from queue import Queue


class Node():
    """class node for k tree"""
    def __init__(self, val, children=None):
        self.val = val
        if children is None:
            children = []
        self.children = children
 
    def __repr__(self):
        """repr function for k-tree"""
        return str(self.val)
    
    def __str__(self):
        """strig repr for node"""
        return self.val


class KTree:
    """class k tree"""
    def __init__(self):
        """init function for k tree class"""
        self.root = None
    
    def __repr__(self):
        """repr function for tree"""
        return str(self.root.val)
    
    def __str__(self):
        """string representation for tree"""
        return str(self.root.val)
    
    def pre_order(self, operation):
        """preorder traversal algoritm"""
        def _walk(node=None):
            if node is None:
                return
            operation(node)

            for item in node.children:
                _walk(item)
        
        if self.root is None:
            return False
        else:
            _walk(self.root)
    
    def post_order(self, operation):
        """postorder traversal algoritm"""
        def _walk(node=None):
            if node is None:
                return

            for item in node.children:
                _walk(item)
            operation(node.val)
        
        if self.root is None:
            return False
        else:
            _walk(self.root)   
    
    def insert(self, value, parent=None):
        """insert value in the tree"""
        # import pdb; pdb.set_trace()
        node = Node(value)
        if self.root is None:
            self.root = node
            return
        if self.root.val == parent or parent is None:
            self.root.children.append(node)
            return

        qu = Queue()

        def campare(node):
            """local function for campare to stuff"""
            if node.val == parent:
                node.children.append(Node(value))
                return True
            for item in node.children:
                qu.enqueue(item)
            return False
        for item in self.root.children:
            qu.enqueue(item)
        top = qu.dequeue()
        found = False
        while top and not found:
            found = campare(top.val)
            top = qu.dequeue()
                     
    def breadth_first_traversal(self, action=None):
        """define function to print nodes in the bredth first order"""
        if self.root is None:
            return False
        action(self.root.val)
        qu = Queue()
        for item in self.root.children:
            # import pdb; pdb.set_trace()
            qu.enqueue(item)
        top = qu.dequeue()
        while top:
            action(top.val)
            if top.val.children:
                for item in top.val.children:
                    qu.enqueue(item)
            top = qu.dequeue()


