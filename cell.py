class Cell:
	grid = None
	row = None
	col = None
	
	north = None
	east = None
	south = None
	west = None
	
	links = None
	
	def __init__(self, grid, col, row):
		self.grid = grid
		self.col = col
		self.row = row
		self.links = []
	
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