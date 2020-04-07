from grid import Grid
from RecursiveBacktracker import RecursiveBacktracker as Algorithm

from clear import Clear

colCount = 5
rowCount = 5
floor = 0

run = True
while run:
	if floor > 0:
		colCount += 2
		rowCount += 2
	
	grid = Grid(colCount, rowCount)
	Algorithm.On(grid)
	
	#TODO: Determine start and end points
	
	clear()
	print("Floor " + str(floor))
	print(grid)
	
	i = input("Press enter for next floor, or type 'exit' to quit: ")
	if i == "exit":
		run = False
	
	floor += 1