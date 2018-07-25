def DFS(g, u, discovered):
    """
    Perform DFS of the undiscovered portion of Graph g starting at Vertex u.
    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be ”discovered” prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result.
    """
    # for every outgoing edge from u
    for e in g.insident_edges(u):
        v = e.opposite(u)
        # v is an unvisited vertex
        if v not in discovered:
            # e is the tree edge that discovered v
            discovered[v] = e
            # recursively explore from v
            DFS(g, v, discovered)    