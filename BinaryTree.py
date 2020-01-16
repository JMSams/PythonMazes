from random import randint
from grid import Grid
from cell import Cell

class BinaryTree:
	name = "Binary Tree"
	supportedGrids = [1]
	
	@staticmethod
	def On(grid):
		for row in range(grid.rowCount):
			for col in range(grid.colCount):
				neighbours = []
				if grid[col, row].north != None:
					neighbours.append(grid[col, row].north)
				if grid[col, row].east != None:
					neighbours.append(grid[col, row].east)
				
				if len(neighbours) == 0:
					continue
				
				grid[col, row].Link(neighbours[randint(0, len(neighbours)-1)])