from random import randint
from grid import Grid
from cell import Cell
from sys import setrecursionlimit

def Mazify(grid):
	visited = []
	
	startX = randint(0, grid.colCount-1)
	startY = randint(0, grid.rowCount-1)
	
	setrecursionlimit(1500)
	BacktrackRecursively(grid, visited, startX, startY)

def BacktrackRecursively(grid, visited, col, row):
	visited.append(grid[col, row])
	
	candidates = []
	if isinstance(grid[col, row].north, Cell) and grid[col, row].north not in visited:
		candidates.append(grid[col, row].north)
	if isinstance(grid[col, row].east, Cell) and grid[col, row].east not in visited:
		candidates.append(grid[col, row].east)
	if isinstance(grid[col, row].south, Cell) and grid[col, row].south not in visited:
		candidates.append(grid[col, row].south)
	if isinstance(grid[col, row].west, Cell) and grid[col, row].west not in visited:
		candidates.append(grid[col, row].west)
	
	while len(candidates) > 0:
		candidate = candidates.pop(randint(0, len(candidates)-1))
		if candidate not in visited:
			grid[col, row].Link(candidate)
			BacktrackRecursively(grid, visited, candidate.col, candidate.row)