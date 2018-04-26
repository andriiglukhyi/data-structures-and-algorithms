from queue import Queue


def print_level_order(tree):
    """function based on breadth tree to travetse tree"""
    qu1 = Queue()
    qu2 = Queue()
    end = ''
    if tree.root is None:
        return False
    end += str(tree.root.val)+" \n "
    for item in tree.root.children:
        qu1.enqueue(item)

    def swap(queue1, queue2):
        """empty queue"""
        nonlocal end
        cur = queue1.dequeue()
        while cur:
            end += str(cur.val.val) + " "
            for item in cur.val.children:
                queue2.enqueue(item)
            cur = queue1.dequeue()
        end+= " \n "    
    while qu1.front:
        swap(qu1, qu2)
        swap(qu2, qu1)
    return end