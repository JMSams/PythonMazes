from random import randint
from grid import Grid

def Mazify(grid):
	set = []
	
	for row in range(grid.rowCount):
		for col in range(grid.colCount):
			if row == grid.rowCount-1 and col == grid.colCount-1:
				continue
			
			set.append(grid[col, row])
			c = randint(0, 1)
			if col == grid.colCount-1:
				c = 1
			elif row == grid.rowCount-1:
				c = 0
			
			if c == 0:
				grid[col, row].Link(grid[col, row].east)
			else:
				i = randint(0, len(set)-1)
				set[i].Link(set[i].north)
				set = []