from random import randint
from maze import Maze

def Sidewinder(rows, cols):
	maze = Maze(rows, cols)
	
	set = []
	
	for row in range(rows):
		for col in range(cols):
			if row == rows-1 and col == cols-1:
				continue
			
			set.append(maze.data[row][col])
			c = randint(0, 1)
			if col == cols-1:
				c = 1
			elif row == rows-1:
				c = 0
			
			if c == 0:
				maze.data[row][col].Link(maze.data[row][col].east)
			else:
				i = randint(0, len(set)-1)
				set[i].Link(set[i].north)
				set = []
	
	return maze