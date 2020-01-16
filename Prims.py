from random import randint
from grid import Grid

class Prims:
	name = "Prims"
	supportedGrids = [1, 2]
	
	@staticmethod
	def On(grid):
		active = []
		
		active.append(grid.randomCell())
		
		while len(active) > 0:
			cell = active[randint(0, len(active)-1)]
			
			available = []
			if cell.north != None and len(cell.north.links) == 0:
				available.append(cell.north)
			if cell.east != None and len(cell.east.links) == 0:
				available.append(cell.east)
			if cell.south != None and len(cell.south.links) == 0:
				available.append(cell.south)
			if cell.west != None and len(cell.west.links) == 0:
				available.append(cell.west)
			
			if len(available) > 0:
				i = randint(0, len(available)-1)
				cell.Link(available[i])
				active.append(available[i])
			else:
				active.remove(cell)