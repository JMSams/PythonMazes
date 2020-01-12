from PIL import Image
from grid import Grid
from Sprites import *

def OutputImage(grid, outname = "output"):
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
	
	image.save(outname + ".png")

def SelectSprite(cell):
	if cell.IsLinked([cell.north, cell.east, cell.south, cell.west]):
		return Sprite_NESW
	elif cell.IsLinked([cell.north, cell.east, cell.south]):
		return Sprite_NES
	elif cell.IsLinked([cell.north, cell.south, cell.west]):
		return Sprite_NSW
	elif cell.IsLinked([cell.north, cell.east, cell.west]):
		return Sprite_NEW
	elif cell.IsLinked([cell.south, cell.east, cell.west]):
		return Sprite_SEW
	elif cell.IsLinked([cell.north, cell.east]):
		return Sprite_NE
	elif cell.IsLinked([cell.north, cell.west]):
		return Sprite_NW
	elif cell.IsLinked([cell.south, cell.east]):
		return Sprite_SE
	elif cell.IsLinked([cell.south, cell.west]):
		return Sprite_SW
	elif cell.IsLinked([cell.north, cell.south]):
		return Sprite_NS
	elif cell.IsLinked([cell.east, cell.west]):
		return Sprite_EW
	elif cell.IsLinked([cell.north]):
		return Sprite_N
	elif cell.IsLinked([cell.east]):
		return Sprite_E
	elif cell.IsLinked([cell.south]):
		return Sprite_S
	elif cell.IsLinked([cell.west]):
		return Sprite_W
	else:
		return Sprite__