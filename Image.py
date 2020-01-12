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
			offset = ((col * cell_size), (image_height - ((row+1) * cell_size)))
			
			#print("Cell ({},{}) offset ({},{})".format(col, row, offset[0], offset[1]))
			
			sprite = SelectSprite(grid[col, row])
			image.paste(sprite, offset)
	
	image.save('output.png')
	print('Saved maze to output.png')

def SelectSprite(cell):
	if cell.IsLinked([cell.north, cell.east, cell.south, cell.west]):
		return Sprite_NESW
	elif cell.IsLinked([cell.north, cell.east, cell.south]):
		return Sprite_NES
	elif cell.IsLinked([cell.north, cell.south, cell.west]):
		return Sprite_NSW
	elif cell.IsLinked([cell.north, cell.south, cell.west]):
		return Sprite_NSW
	else:
		return Sprite__