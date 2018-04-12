
class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def __repr__(self):
        return self.val

    def __str__(self):
        return self.val


class BST:
    def __init__(self, iter=[]):
        self.root = None
        
        for item in iter:
            self.insert(item)

    def __repr__(self):
        return '<BST Root {}>'.format(self.root.val)

    def __str__(self):
        return self.root.val

    def in_order(self, operation):
        """in_order traversal"""
        def _walk(node=None):
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)
            operation(node.val)

            if node.right is not None:
                _walk(node.right)

        if self.root is None:
            return False
        else:
            _walk(self.root)
    
    def insert(self, val):
        node = Node(val)

        def _insert(current, node):
            """isert node in bst"""
            if node.val >= current.val:
                if current.right is None:
                    current.right = node
                else:
                    current = current.right
                    _insert(current, node)
            if node.val < current.val:
                if current.left is None:
                    current.left = node
                else:
                    current = current.left
                    _insert(current, node)

        if self.root is None:
            self.root = node
            return node
        else:
            current = self.root
            _insert(current, node)

    def pre_order(self, operation):
        """preorder traversal"""
        def _walk(node=None):
            if node is None:
                return
            operation(node.val)

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)
        
        if self.root is None:
            return False
        else:
            _walk(self.root)
    
    def post_order(self, operation):
        """postorder traversal"""
        def _walk(node=None):
            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)
            operation(node.val)

            if node is None:
                return
        
        if self.root is None:
            return False
        else:
            _walk(self.root)

