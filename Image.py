from PIL import Image

from grid import Grid

wall_width = 1
corridor_width = 3

def OutputImage(grid):
	image_width = (grid.colCount * corridor_width) + (grid.colCount * wall_width) + wall_width
	image_height = (grid.rowCount * corridor_width) + (grid.rowCount * wall_width) + wall_width
	
	image = Image.new('RGBA', (image_width, image_height), 'black')
	
	for row in range(grid.rowCount):
		for col in range(grid.colCount);
			pass# TODO: Draw grid to image
	
	image.save('output.png')
	print('Saved maze to output.png')