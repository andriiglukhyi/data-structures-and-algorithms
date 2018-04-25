from queue import Queue


def print_level_order(tree):
    """function based on breadth tree to travetse tree"""
    qu1 = Queue()
    qu2 = Queue()
    end = ''
    if tree.root is None:
        return False
    end += str(tree.root.val)+"\n"
    for item in tree.root.children:
        qu1.enqueue(item)

    def campare(qu1, qu2):
        """empty queue"""
        nonlocal end
        cur = qu1.dequeue()
        while cur:
            end += str(cur.val.val) + " "
            for item in cur.val.children:
                qu2.enqueue(item)
            cur = qu1.dequeue()
        end+= "\n"

    while qu1.front or qu2.front:
        if qu1.front is None:
            campare(qu2, qu1)
        else:
            campare(qu1, qu2)
    return end