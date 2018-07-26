def BFS(g, s, discovered):
    """
    Perform BFS of the undiscovered portion of Graph g starting at Vertex s.
    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the BFS (s should be mapped to None prior to the call).
    Newly discovered vertices will be added to the dictionary as a result.
    """
    # first level includes only s
    level = [s]
    while len(level)>0:
        # prepare to gather newly found vertices
        next_level = []
        # for every outgoing edge from u
        for u in level:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                # v is an unvisited vertex
                if v not in discovered:
                    # e is the tree edge that discovered v
                    discovered[v] = e
                    # v will be further considered in next pass
                    next_level.append(v)
        # relabel ’next’ level to become current
        level = next_level
    
