from random import randint
from grid import Grid

class Prims:
	name = "Prims"
	supportedGrids = [1, 2]
	
	@staticmethod
	def On(grid):
		visited = []
		
		visited.append(grid.randomCell())
		
		while len(visited) < (grid.cellCount()):
			neighbours = Prims.getNeighbours(visited)
			pair = neighbours.pop(randint(0, len(neighbours)-1))
			visited.append(pair[1])
			pair[0].Link(pair[1])
	
	@staticmethod
	def getNeighbours(visited):
		rv = []
		
		for cell in visited:
			if cell.north != None and cell.north not in visited:
				rv.append((cell, cell.north))
			if cell.east != None and cell.east not in visited:
				rv.append((cell, cell.east))
			if cell.south != None and cell.south not in visited:
				rv.append((cell, cell.south))
			if cell.west != None and cell.west not in visited:
				rv.append((cell, cell.west))
		
		return rv