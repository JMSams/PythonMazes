from random import randint
from maze import Maze
from cell import Cell

def RecursiveBacktracker(rows, cols):
	maze = Maze(rows, cols)
	visited = []
	
	startX = randint(0, cols-1)
	startY = randint(0, rows-1)
	
	BacktrackRecursively(maze, visited, startY, startX)
	
	return maze

def BacktrackRecursively(maze, visited, row, col):
	visited.append(maze.data[row][col])
	
	candidates = []
	if isinstance(maze.data[row][col].north, Cell) and maze.data[row][col].north not in visited:
		candidates.append(maze.data[row][col].north)
	if isinstance(maze.data[row][col].east, Cell) and maze.data[row][col].east not in visited:
		candidates.append(maze.data[row][col].east)
	if isinstance(maze.data[row][col].south, Cell) and maze.data[row][col].south not in visited:
		candidates.append(maze.data[row][col].south)
	if isinstance(maze.data[row][col].west, Cell) and maze.data[row][col].west not in visited:
		candidates.append(maze.data[row][col].west)
	
	while len(candidates) > 0:
		candidate = candidates.pop(randint(0, len(candidates)-1))
		if candidate not in visited:
			maze.data[row][col].Link(candidate)
			BacktrackRecursively(maze, visited, candidate.row, candidate.column)