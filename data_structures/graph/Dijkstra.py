from heapdict import heapdict

def shortest_path_length(g, src):
    """
    Compute shortest-path distances from src to reachable vertices of g.
    Graph g can be undirected or directed, but must be weighted such that
    e.element() returns a numeric weight for each edge e.
    Return dictionary mapping each reachable vertex to its distance from src.
    """
    d = {} # d[v] upper bound from src
    cloud = {} # map reacheble v to it's d[v] value
    pq = AdaptableHeapPriorityQueue() # priority queue |||  obj = hd.popitem()
    pglocator = {} # map from vertex to it's pg locator
    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float('inf') # positive infonity
        pglocator[v] = pq.add(d[v], v)
    
    while not pq.is_empty():
        key, u = pq.remove.min()
        cloud[u] = key
        del pglocator[u]
        for e in g.encident_edges(u):
            v = g.opposite(e)
            if v not in cloud:
                # perform relaxation step on edge (u,v)
                wgt = e.element()
                if d[u] + wgt < d[v]:
                    d[v]= d[u] + wgt
                    pq.update(pglocator[v], d[v], v)
    return cloud