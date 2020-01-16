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

def SelectSprite(cell):
	if cell.IsLinked([cell.north, cell.east, cell.south, cell.west]):
		return NESW
	elif cell.IsLinked([cell.north, cell.east, cell.south]):
		return NES
	elif cell.IsLinked([cell.north, cell.south, cell.west]):
		return NSW
	elif cell.IsLinked([cell.north, cell.east, cell.west]):
		return NEW
	elif cell.IsLinked([cell.south, cell.east, cell.west]):
		return SEW
	elif cell.IsLinked([cell.north, cell.east]):
		return NE
	elif cell.IsLinked([cell.north, cell.west]):
		return NW
	elif cell.IsLinked([cell.south, cell.east]):
		return SE
	elif cell.IsLinked([cell.south, cell.west]):
		return SW
	elif cell.IsLinked([cell.north, cell.south]):
		return NS
	elif cell.IsLinked([cell.east, cell.west]):
		return EW
	elif cell.IsLinked([cell.north]):
		return N
	elif cell.IsLinked([cell.east]):
		return E
	elif cell.IsLinked([cell.south]):
		return S
	elif cell.IsLinked([cell.west]):
		return W
	else:
		return D