class Cell:
	row = None
	col = None
	
	north = None
	east = None
	south = None
	west = None
	
	links = None
	
	def __init__(self, col, row):
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
		return (other in self.links)