from termcolor import colored
from cell import Cell
from options import *

class Maze:
	columns = 3
	rows = 3
	
	data = []
	
	def __init__(self, rows, columns):
		self.columns = columns
		self.rows = rows
		
		for y in range(rows):
			row = []
			for x in range(columns):
				row.append(Cell(y, x))
			self.data.append(row)
		
		for y in range(rows):
			for x in range(columns):
				if x > 0:
					self.data[y][x].west = self.data[y][x-1]
				if x < columns-1:
					self.data[y][x].east = self.data[y][x+1]
				if y > 0:
					self.data[y][x].south = self.data[y-1][x]
				if y < rows-1:
					self.data[y][x].north = self.data[y+1][x]
	
	def __str__(self):
		rv = ""
		
		rv += colored("+", GRID_COLOUR)
		for col in range(self.columns):
			rv += colored("---+", GRID_COLOUR)
		rv += "\n"

		for row in range(self.rows-1, -1, -1):
			rv += colored("|", GRID_COLOUR)
			for col in range(self.columns):
				rv += (str(col) + "," + str(row)) if SHOW_COORDS else "   "
				if col == self.columns-1:
					rv += colored("|", GRID_COLOUR)
				else:
				  rv += " " if self.data[row][col].east in self.data[row][col].links else colored("|", GRID_COLOUR)
			rv += "\n"
			
			rv += colored("+", GRID_COLOUR)
			for col in range(self.columns):
				rv += colored("   +" if self.data[row][col].south in self.data[row][col].links else "---+", GRID_COLOUR)
			rv += "\n"
		
		return rv
	
	def Draw(self):
		pass