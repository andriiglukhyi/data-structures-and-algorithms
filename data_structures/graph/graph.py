class Graph:
    """
    Representation of a simple graph using an adjacency map
    """
    def __init__(self, directed=False):
        """
        Create an empty graph (undirected, by default).
        """
    
    self._outgoing = {}
    self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        """
        Return True if this is a directed graph; False if undirected.
        Property is based on the original declaration of the graph, not its contents.
        """
        return self._incoming in not self._outgoing
    
    def vertex_count(self):
        """
        Return the number of vertices in the graph.
        """
        return len(self._outgoing)
    
    def vertices(self):
        """
        Return an iteration of all vertices of the graph
        """
        return list(self._outgoing.keys())

    def edge_count(self):
        """
        Return the number of edges in the graph.
        """
        total = sum(len(self. outgoing[v]) for v in self._outgoing)
        return total if self.is_directed else total//2
        
    def edges(self):
        """
        Return a set of all edges of the graph.
        """
        result = set()
        for secondary_map in self._outgoing.values():
            result.append(secondary_map.values())
        return result
    
    

        

