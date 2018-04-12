def find_maximum_value(tree):
    """function to find max value"""
    if tree.root is None:
        return False
    mx = tree.root.val
    root = tree.root

    def _walk(root):
        nonlocal mx
        if root is None:
            return mx
        if root.val > mx:
            mx = root.val
        if root.left is not None:
            _walk(root.left)
        if root.right is not None:
            _walk(root.right)
    _walk(root)
    return mx