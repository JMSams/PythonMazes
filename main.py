from grid import Grid
from RecursiveBacktracker import RecursiveBacktracker as Algorithm

import clear

colCount = 21
rowCount = 7

grid = Grid(colCount, rowCount)
Algorithm.On(grid)

print(grid)