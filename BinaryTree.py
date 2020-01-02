from random import randint
from maze import Maze

def BinaryTree(rows, cols):
	maze = Maze(rows, cols)
	
	for row in range(rows):
		for col in range(cols):
			if col == cols-1:
				if row == rows-1:
					# North east corner, no link
					pass
				else:
					# East edge, link north
					maze.data[row][col].Link(maze.data[row][col].north)
			elif row == rows-1:
				# North edge, link east
				maze.data[row][col].Link(maze.data[row][col].east)
			else:
				# Rest of maze, link randomly
				maze.data[row][col].Link(maze.data[row][col].east if randint(0,1) == 1 else maze.data[row][col].north)
	
	return maze