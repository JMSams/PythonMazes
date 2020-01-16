from random import randint
from grid import Grid
from cubeGrid import CubeGrid
from cell import Cell
from sys import setrecursionlimit

class RecursiveBacktracker:
	name = "Recursive Backtracker"
	supportedGrids = [1, 2]
	
	@staticmethod
	def On(grid):
		setrecursionlimit(5000)
		
		visited = []
		
		startX = randint(0, grid.colCount-1)
		startY = randint(0, grid.rowCount-1)
		
		if isinstance(grid, CubeGrid):
			startF = randint(0, 5)
			RecursiveBacktracker.BacktrackRecursivelyCubed(grid, visited, startF, startX, startY)
		else:
			RecursiveBacktracker.BacktrackRecursively(grid, visited, startX, startY)
	
	@staticmethod
	def BacktrackRecursively(grid, visited, col, row):
		visited.append(grid[col, row])
		
		candidates = []
		if (grid[col, row].north != None) and grid[col, row].north not in visited:
			candidates.append(grid[col, row].north)
		if (grid[col, row].east != None) and grid[col, row].east not in visited:
			candidates.append(grid[col, row].east)
		if (grid[col, row].south != None) and grid[col, row].south not in visited:
			candidates.append(grid[col, row].south)
		if (grid[col, row].west != None) and grid[col, row].west not in visited:
			candidates.append(grid[col, row].west)
		
		while len(candidates) > 0:
			candidate = candidates.pop(randint(0, len(candidates)-1))
			if candidate not in visited:
				grid[col, row].Link(candidate)
				RecursiveBacktracker.BacktrackRecursively(grid, visited, candidate.col, candidate.row)
	
	@staticmethod
	def BacktrackRecursivelyCubed(grid, visited, face, col, row):
		visited.append(grid[face, col, row])
		
		candidates = []
		if (grid[face, col, row].north != None) and grid[face, col, row].north not in visited:
			candidates.append(grid[face, col, row].north)
		if (grid[face, col, row].east != None) and grid[face, col, row].east not in visited:
			candidates.append(grid[face, col, row].east)
		if (grid[face, col, row].south != None) and grid[face, col, row].south not in visited:
			candidates.append(grid[face, col, row].south)
		if (grid[face, col, row].west != None) and grid[face, col, row].west not in visited:
			candidates.append(grid[face, col, row].west)
		
		while len(candidates) > 0:
			candidate = candidates.pop(randint(0, len(candidates)-1))
			if candidate not in visited:
				grid[face, col, row].Link(candidate)
				RecursiveBacktracker.BacktrackRecursivelyCubed(grid, visited, candidate.face, candidate.col, candidate.row)