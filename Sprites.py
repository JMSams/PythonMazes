from cubeCell import CubeCell
from PIL import Image
import os

dirname = os.path.dirname(__file__)

CellSize = 16

SE	= Image.open(os.path.join(dirname, 'Sprites/sprite_00.png'), 'r')
SEW	= Image.open(os.path.join(dirname, 'Sprites/sprite_01.png'), 'r')
SW	= Image.open(os.path.join(dirname, 'Sprites/sprite_02.png'), 'r')
S	= Image.open(os.path.join(dirname, 'Sprites/sprite_03.png'), 'r')
NES	= Image.open(os.path.join(dirname, 'Sprites/sprite_04.png'), 'r')
NESW= Image.open(os.path.join(dirname, 'Sprites/sprite_05.png'), 'r')
NSW	= Image.open(os.path.join(dirname, 'Sprites/sprite_06.png'), 'r')
NS	= Image.open(os.path.join(dirname, 'Sprites/sprite_07.png'), 'r')
NE	= Image.open(os.path.join(dirname, 'Sprites/sprite_08.png'), 'r')
NEW	= Image.open(os.path.join(dirname, 'Sprites/sprite_09.png'), 'r')
NW	= Image.open(os.path.join(dirname, 'Sprites/sprite_10.png'), 'r')
N	= Image.open(os.path.join(dirname, 'Sprites/sprite_11.png'), 'r')
E	= Image.open(os.path.join(dirname, 'Sprites/sprite_12.png'), 'r')
EW	= Image.open(os.path.join(dirname, 'Sprites/sprite_13.png'), 'r')
W	= Image.open(os.path.join(dirname, 'Sprites/sprite_14.png'), 'r')
D	= Image.open(os.path.join(dirname, 'Sprites/sprite_15.png'), 'r')

CubeN	= Image.open(os.path.join(dirname, 'Sprites/sprite_16.png'), 'r')
CubeE	= Image.open(os.path.join(dirname, 'Sprites/sprite_17.png'), 'r')
CubeS	= Image.open(os.path.join(dirname, 'Sprites/sprite_18.png'), 'r')
CubeW	= Image.open(os.path.join(dirname, 'Sprites/sprite_19.png'), 'r')

def SelectSprite(cell):
	rv = []
	
	if cell.IsLinked([cell.north, cell.east, cell.south, cell.west]):
		rv.append(NESW)
	elif cell.IsLinked([cell.north, cell.east, cell.south]):
		rv.append(NES)
	elif cell.IsLinked([cell.north, cell.south, cell.west]):
		rv.append(NSW)
	elif cell.IsLinked([cell.north, cell.east, cell.west]):
		rv.append(NEW)
	elif cell.IsLinked([cell.south, cell.east, cell.west]):
		rv.append(SEW)
	elif cell.IsLinked([cell.north, cell.east]):
		rv.append(NE)
	elif cell.IsLinked([cell.north, cell.west]):
		rv.append(NW)
	elif cell.IsLinked([cell.south, cell.east]):
		rv.append(SE)
	elif cell.IsLinked([cell.south, cell.west]):
		rv.append(SW)
	elif cell.IsLinked([cell.north, cell.south]):
		rv.append(NS)
	elif cell.IsLinked([cell.east, cell.west]):
		rv.append(EW)
	elif cell.IsLinked([cell.north]):
		rv.append(N)
	elif cell.IsLinked([cell.east]):
		rv.append(E)
	elif cell.IsLinked([cell.south]):
		rv.append(S)
	elif cell.IsLinked([cell.west]):
		rv.append(W)
	else:
		rv.append(D)
	
	if isinstance(cell, CubeCell):
		if cell.row == 0:
			rv.append(CubeS)
		elif cell.row == cell.grid.cubeSize-1:
			rv.append(CubeN)
		if cell.col == 0:
			rv.append(CubeW)
		elif cell.col == cell.grid.cubeSize-1:
			rv.append(CubeE)
	
	return tuple(rv)