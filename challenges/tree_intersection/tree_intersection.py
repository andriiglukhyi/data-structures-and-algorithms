from hash_table import HashTable


def tree_intersection(tree1, tree2):
    """function should accept two bt as an argument and return intersections"""
    if tree1.root is None or tree2.root is None:
        return False
    table = HashTable()
    tree1.pre_order(table.set)
    arr = []
    
    def check(value):
        number = table.hash_key(str(value))
        if type(table.buckets[number]) == dict:
            arr.append(value)
    tree2.in_order(check)
    return arr

