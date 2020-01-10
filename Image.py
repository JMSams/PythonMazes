from PIL import Image

from grid import Grid

wall_width = 1
corridor_width = 3

def OutputImage(grid):
	image_width = (grid.colCount * corridor_width) + (grid.colCount * wall_width) + wall_width
	image_height = (grid.rowCount * corridor_width) + (grid.rowCount * wall_width) + wall_width
	
	image = Image.new('RGBA', (image_width, image_height), 'black')
	img = image.load()
	
	for x in range(image_width):
		for y in range(image_height):
			if (x % (corridor_width+wall_width) != 0) and (y % (corridor_width+wall_width) != 0):
				img[x, y] = (255, 255, 255, 255)
	
	for row in range(grid.rowCount):
		for col in range(grid.colCount):
			if grid[col, row].IsLinked(grid[col, row].east):
				pass#TODO: draw eastern wall
			if grid[col, row].IsLinked(grid[col, row].south):
				pass#TODO: draw southern wall
	
	image.save('output.png')
	print('Saved maze to output.png')