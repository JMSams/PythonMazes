from random import randint

from grid import Grid
from RecursiveBacktracker import RecursiveBacktracker as Algorithm

from clear import Clear

colCount = 5
rowCount = 5
floor = 0

# Increment floor size every x floors
x = 3

startCell = (2,2)
endCell = (-1,-1)

run = True
while run:
    if floor > 0 and floor % x == 0:
        colCount += 2
        rowCount += 2
        #TODO: startCell and endCell should be shifted.  Goal being to keep the center point in the center rather than growing towards, for eg, the north-east
        endCell = (endCell[0]+1, endCell[1]+1)
    
    grid = Grid(colCount, rowCount)
    
    if floor > 0:
        startCell = endCell
    
    Algorithm.On(grid, startCell)
    
    #TODO: endCell should be a dead end from the current grid, preferably far away from startCell
    endCell = grid.randomDeadend().coord()
    while endCell == startCell:
        endCell = grid.randomDeadend().coord()
    
    grid[startCell].content = "S"
    grid[endCell].content = "E"
    
    Clear()
    print("Floor " + str(floor))
    print(grid)
    grid.Draw("output/Floor_" + str(floor))
    
    i = input("Press enter for next floor, or type 'exit' to quit: ")
    if i == "exit":
        run = False
    
    floor += 1