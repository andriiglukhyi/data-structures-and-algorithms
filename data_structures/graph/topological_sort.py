def topologocal_sort(g):
    """
    Return a list of verticies of directed acyclic graph g in topological order.
    If graph g has a cycle, the result will be incomplete
    """
    # a list of vertices placed in topological order
    topo = []
    # list of vertices that have no remaining constraints
    ready = []
    # keep track of in-degree for each vertex
    incount = {}
    for u in g.vertices():
        # parameter requests incoming degree
        incount[u] = g.degree(u, False)
        # if u has no incoming edges,
        if incount[u] == 0:
            # it is free of constraints
            ready.append(u)
    while len(ready) > 0:
        # u is free of constraints
        u = ready.pop()
        # add u to the topological order
        topo.append(u)
        for e in g.incident_edges(u):
            # consider all outgoing neighbors of u
            v = e.opposite(u)
            # v has one less constraint without u
            incount[v] -= 1
            if incount[v] == 0:
                ready.append(v)
    return topo