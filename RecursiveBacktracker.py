from random import randint
from grid import Grid
from cell import Cell
from sys import setrecursionlimit

class RecursiveBacktracker:
	@staticmethod
	def On(grid, startCell=None):
		setrecursionlimit(8000)
		RecursiveBacktracker.BacktrackRecursively(grid, [], grid.randomCell() if startCell == None else startCell)
	
	@staticmethod
	def BacktrackRecursively(grid, visited, cell):
		visited.append(cell)
		
		candidates = []
		if (cell.north != None) and cell.north not in visited:
			candidates.append(cell.north)
		if (cell.east != None) and cell.east not in visited:
			candidates.append(cell.east)
		if (cell.south != None) and cell.south not in visited:
			candidates.append(cell.south)
		if (cell.west != None) and cell.west not in visited:
			candidates.append(cell.west)
		
		while len(candidates) > 0:
			candidate = candidates.pop(randint(0, len(candidates)-1))
			if candidate not in visited:
				cell.Link(candidate)
				RecursiveBacktracker.BacktrackRecursively(grid, visited, candidate)