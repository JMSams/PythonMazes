class Cell:
	row = None
	column = None
	
	content = " "
	
	north = None
	east = None
	south = None
	west = None
	links = []
	
	def __init__(self, row, col):
		self.row = row
		self.column = col
		self.links = []
	
	def Link(self, other, bidi=True):
		if isinstance(other, Cell):
			self.links.append(other)
			if bidi:
				other.Link(self, False)
	
	def __str__(self):
		return "({},{})".format(self.column, self.row)
	
	def __eq__(self, other):
		if not isinstance(other, Cell):
			return False
		return (self.row == other.row) and (self.column == other.column)
	def __ne__(self, other):
		return not self.__eq__(other)