from random import randint
from grid import Grid

class Sidewinder:
	name = "Sidewinder"
	supportedGrids = [1]
	
	@staticmethod
	def On(grid):
		set = []
		
		for row in grid.eachRow():
			for cell in row:
				set.append(cell)
				
				atEasternBoundary = (cell.east == None)
				atNorthernBoundary = (cell.north == None)
				
				closeOut = atEasternBoundary or (not atNorthernBoundary and randint(0,1) == 0)
				
				if closeOut:
					member = set[randint(0, len(set)-1)]
					member.Link(member.north)
					set.clear()
				else:
					cell.Link(cell.east)