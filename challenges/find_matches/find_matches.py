def find_matches(tree, value=None):
    """function to find all the value"""
    if tree.root is None or value is None:
        return False
    lst = []
    
    def campare(node):
        """campare value of the node to main value"""
        nonlocal lst
        if node.val == value:
            lst.append(node)
    
    tree.pre_order(campare)
    return lst