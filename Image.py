from PIL import Image
from grid import Grid
from Sprites import *

def OutputImage(grid):
	cell_size = 16
	image_width = grid.colCount * cell_size
	image_height = grid.rowCount * cell_size
	
	image = Image.new('RGBA', (image_width, image_height), 'black')
	
	for row in range(grid.rowCount):
		for col in range(grid.colCount):
			sprite = SelectSprite(grid[col, row])
			#TODO: Paste sprite into image
	
	image.save('output.png')
	print('Saved maze to output.png')

def SelectSprite(cell):
	if cell.IsLinked([cell.north, cell.east, cell.south, cell.west]):
		return Sprites_NESW
	#TODO: Return other sprites
	else:
		return Sprites__