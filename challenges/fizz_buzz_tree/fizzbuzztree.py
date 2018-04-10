
def fizz_buzz_tree(tree):
    """function takes a binary tree as an argument """
    
    def _walk(node=None):
        if node is None:
            return
        if node.left is not None:
            _walk(node.left)
        if node.val % 15 == 0:
            node.val = "FizzBuzz"
        elif node.val % 3 == 0:
            node.val = "Fizz"
        elif node.val % 5 == 0:
            node.val = "Buzz"
        if node.right is not None:
            _walk(node.right)
    if tree.root is None:
        return False
    else:
        _walk(tree.root)
    return tree
