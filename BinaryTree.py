from random import randint
from grid import Grid
from cell import Cell

class BinaryTree:
	name = "Binary Tree"
	supportedGrids = [1]
	
	@staticmethod
	def On(grid):
		for cell in grid.eachCell():
			neighbours = []
			if cell.north != None:
				neighbours.append(cell.north)
			if cell.east != None:
				neighbours.append(cell.east)
			
			if len(neighbours) == 0:
				continue
			
			cell.Link(neighbours[randint(0, len(neighbours)-1)])