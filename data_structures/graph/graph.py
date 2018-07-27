from vertex import Vertex
from edge import Edge

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
        return self._incoming is not self._outgoing
    
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
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed else total//2
        
    def edges(self):
        """
        Return a set of all edges of the graph.
        """
        result = set()
        for secondary_map in self._outgoing.values():
            result.add(secondary_map.values())
        return result
    
    def get_edge(self, u, v):
        """
        Return the edge from u to v, or None if not adjacent.
        """
        if u in self._outgoing:
            return self._outgoing[u].get(v)
        return False
    
    def degree(self, v, outgoing=True):
        """
        Return number of (outgoing) edges incident to vertex v in the graph.
        """
        adj = self._outgoing if outgoing else self._incoming
        if v in adj:
            return len(adj.get())
        return False

    def incident_edges(self, v, outgoing=True):
        """
        Return all (outgoing) edges incident to vertex v in the graph.
        If graph is directed, optional parameter used to request incoming edges.
        """
        adj = self._outgoing if outgoing else self._incoming
        if v in adj:
            for edge in adj[v].values():
                yield edge
        return False
    
    def insert_vertex(self, x=None):
        """
        Insert and return a new Vertex with element x.
        """
        v = Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed:
            self._incoming = {}
        return v

    
    def insert_edge(self, u, v, x=None):
        """
        Insert and return a new Edge from u to v with auxiliary element x.
        """
        e = Edge(u, v, x)
        self._incoming[u][v] = e
        self._outgoing[u][v] = e
