from random import randint
from maze import Maze

def RecursiveBacktracker(rows, cols):
	maze = Maze(rows, cols)
	visited = []
	
	startX = randint(0, cols-1)
	startY = randint(0, rows-1)
	
	BacktrackRecursively(maze, visited, startY, startX)
	
	return maze

def BacktrackRecursively(maze, visited, row, col):
	visited.append(maze.data[row][col])
	
	pass