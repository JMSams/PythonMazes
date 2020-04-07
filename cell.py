class Cell:
    def __init__(self, grid, col, row):
        self.grid = grid
        self.col = col
        self.row = row

        self.links = []

        self.north = None
        self.east = None
        self.south = None
        self.west = None

        self.content = " "
    
    def coord(self):
        return (self.col, self.row)
    
    def Link(self, other, bidi=True):
        if isinstance(other, Cell):
            self.links.append(other)
            if bidi:
                other.Link(self, False)
    
    def Unlink(self, other, bidi=True):
        if isinstance(other, Cell):
            self.links.remove(other)
            if bidi:
                other.Unlink(self, False)
    
    def IsLinked(self, other):
        if isinstance(other, list):
            rv = True
            for o in other:
                rv = rv and self.IsLinked(o)
            return rv
        elif isinstance(other, Cell):
            return (other in self.links)