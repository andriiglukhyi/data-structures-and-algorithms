class Vertex:
    __slots__ = 'element'
    """
    Ligthweight verttex structure for graph
    """
    def __init__(self, x):
        """
        Do not call constractor dorectly. Use Graph's insert_vertex(x)
        """
        self.element = x
    
    def element(self):
        """
        Return element associated with this vertex
        """
        return self.element
    
    def __hash__(self):
        """
        will allow vertex to be a map/set key
        """
        return hash(id(self))