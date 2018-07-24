class Vertex:
    """
    Ligthweight verttex structure for graph
    """
    __slots__ = '_element'

    def __init__(self, x):
        """
        Do not call constractor dorectly. Use Graph's insert_vertex(x)
        """
        self._element = x
        
    def element(self):
        """
        Return element associated with this vertex
        """
        return self._element
    
    def __hash__(self):
        """
        will allow vertex to be a map/set key
        """
        return hash(id(self))