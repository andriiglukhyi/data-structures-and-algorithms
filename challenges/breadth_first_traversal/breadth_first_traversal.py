from queue import Queue


def breadth_first_traversal(tree, action=print):
    """define function to print nodes in the bredth first order"""
    if tree.root is None:
        return False
    action(tree.root.val)
    qu = Queue()
    if tree.root.left:
        qu.enqueue(tree.root.left)
    if tree.root.right:
        qu.enqueue(tree.root.right)
    top = qu.front
    while top:
        node = top.val
        action(node.val)
        if node.left:
            qu.enqueue(node.left)
        if node.right:
            qu.enqueue(node.right)
        top = top.next
    

    



