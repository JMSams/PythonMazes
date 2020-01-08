from random import randint
from cell import Cell

class Grid:
	colCount = -1
	rowCount = -1
	
	grid = None
	
	def __init__(self, colCount, rowCount):
		self.colCount = colCount
		self.rowCount = rowCount
		
		self.grid = []
		self.PrepareGrid()
		self.ConfigureGrid()
	
	def PrepareGrid(self):
		for col in range(self.colCount):
			newCol = []
			for row in range(self.rowCount):
				newCol.append(Cell(col, row))
			self.grid.append(newCol)
	
	def ConfigureGrid(self):
		for row in range(self.rowCount):
			for col in range(self.colCount):
				self[col, row].north = self[col, row+1]
				self[col, row].south = self[col, row-1]
				self[col, row].east = self[col+1, row]
				self[col, row].west = self[col-1, row]
	
	def __getitem__(self, coord):
		col,row = coord
		if col < 0:
			return None
		elif col >= self.colCount:
			return None
		elif row < 0:
			return None
		elif row >= self.rowCount:
			return None
		else:
			return self.grid[col][row]
	
	def orphans(self):
		rv = []
		for row in range(self.rowCount):
			for col in range(self.colCount):
				if len(self[col, row].links) == 0:
					rv.append(self[col, row])
		return rv
	
	def deadends(self):
		rv = []
		for row in range(self.rowCount):
			for col in range(self.colCount):
				if len(self[col, row].links) == 1:
					rv.append(self[col, row])
		return rv
	
	def randomCell(self):
		return self[randint(0, self.colCount-1), randint(0, self.rowCount-1)]
	
	def __str__(self):
		rv = ""
		
		rv += "+"
		for col in range(self.colCount):
			rv += "---+"
		rv += "\n"

		for row in range(self.rowCount-1, -1, -1):
			rv += "|"
			for col in range(self.colCount):
				rv += "   "
				if col == self.colCount-1:
					rv += "|"
				else:
				  rv += " " if self[col, row].east in self[col, row].links else "|"
			rv += "\n"
			
			rv += "+"
			for col in range(self.colCount):
				rv += "   +" if self[col, row].south in self[col, row].links else "---+"
			rv += "\n"
		
		return rv
	
	def Draw(self):
		pass