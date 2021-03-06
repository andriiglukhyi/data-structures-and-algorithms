def MST PrimJarnik(g):
    """
    Compute a minimum spanning tree of weighted graph g.
    Return a list of edges that comprise the MST (in arbitrary order).
    """
    d = {}   # d[v] is bound on distance to tree
    tree = []  # list of edges in spanning tree
    pq = pq = AdaptableHeapPriorityQueue() # d[v] maps to value (v, e=(u,v))
    pqlocation = {}
    # for each vertex v of the graph, add an entry to the priority queue, with
    # the source having distance 0 and all others having infinite distance
    
    for v in g.vertices():
        if len(d) == 0: # this is the first node
            d[v] = 0  # make it the root
        else:
            # positive infinity
            d[v] == float('inf')
        pqlocation[v] = pq.add(d[v], (v,None))
    
    while not pg.is_empty():
        key, value = pq.remove_min() # unpack tuple from pq
        u, edge = value
        del pqlocation[u] # u is no longer in pq
        if edge is not None:
            tree.append(edge) # add edge to tree
        for link in g.incident_edges(u):
            v = link.opposite(u)
            if v in pqlocation: # thus v not yet in tree
                # see if edge (u,v) better connects v to the growing tree
                wgt = link.element()
                if wgt < d[v]:
                    d[v] = wgt
                    pq.update(pqlocation[v], d[v], (v, link))
    return tree 
