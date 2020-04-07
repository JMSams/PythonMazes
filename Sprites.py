from PIL import Image
import os

dirname = os.path.dirname(__file__)

CellSize = 16

SE  = Image.open(os.path.join(dirname, 'Sprites/sprite_00.png'), 'r')
SEW = Image.open(os.path.join(dirname, 'Sprites/sprite_01.png'), 'r')
SW  = Image.open(os.path.join(dirname, 'Sprites/sprite_02.png'), 'r')
S   = Image.open(os.path.join(dirname, 'Sprites/sprite_03.png'), 'r')
NES = Image.open(os.path.join(dirname, 'Sprites/sprite_04.png'), 'r')
NESW= Image.open(os.path.join(dirname, 'Sprites/sprite_05.png'), 'r')
NSW = Image.open(os.path.join(dirname, 'Sprites/sprite_06.png'), 'r')
NS  = Image.open(os.path.join(dirname, 'Sprites/sprite_07.png'), 'r')
NE  = Image.open(os.path.join(dirname, 'Sprites/sprite_08.png'), 'r')
NEW = Image.open(os.path.join(dirname, 'Sprites/sprite_09.png'), 'r')
NW  = Image.open(os.path.join(dirname, 'Sprites/sprite_10.png'), 'r')
N   = Image.open(os.path.join(dirname, 'Sprites/sprite_11.png'), 'r')
E   = Image.open(os.path.join(dirname, 'Sprites/sprite_12.png'), 'r')
EW  = Image.open(os.path.join(dirname, 'Sprites/sprite_13.png'), 'r')
W   = Image.open(os.path.join(dirname, 'Sprites/sprite_14.png'), 'r')
D   = Image.open(os.path.join(dirname, 'Sprites/sprite_15.png'), 'r')

Start = Image.open(os.path.join(dirname, 'Sprites/Start.png'), 'r')
End = Image.open(os.path.join(dirname, 'Sprites/End.png'), 'r')

def SelectSprite(cell):
    baseImage = Image.new('RGBA', (16, 16))
    if cell.IsLinked([cell.north, cell.east, cell.south, cell.west]):
        baseImage.paste(NESW, (0,0))
    elif cell.IsLinked([cell.north, cell.east, cell.south]):
        baseImage.paste(NES, (0,0))
    elif cell.IsLinked([cell.north, cell.south, cell.west]):
        baseImage.paste(NSW, (0,0))
    elif cell.IsLinked([cell.north, cell.east, cell.west]):
        baseImage.paste(NEW, (0,0))
    elif cell.IsLinked([cell.south, cell.east, cell.west]):
        baseImage.paste(SEW, (0,0))
    elif cell.IsLinked([cell.north, cell.east]):
        baseImage.paste(NE, (0,0))
    elif cell.IsLinked([cell.north, cell.west]):
        baseImage.paste(NW, (0,0))
    elif cell.IsLinked([cell.south, cell.east]):
        baseImage.paste(SE, (0,0))
    elif cell.IsLinked([cell.south, cell.west]):
        baseImage.paste(SW, (0,0))
    elif cell.IsLinked([cell.north, cell.south]):
        baseImage.paste(NS, (0,0))
    elif cell.IsLinked([cell.east, cell.west]):
        baseImage.paste(EW, (0,0))
    elif cell.IsLinked([cell.north]):
        baseImage.paste(N, (0,0))
    elif cell.IsLinked([cell.east]):
        baseImage.paste(E, (0,0))
    elif cell.IsLinked([cell.south]):
        baseImage.paste(S, (0,0))
    elif cell.IsLinked([cell.west]):
        baseImage.paste(W, (0,0))
    else:
        baseImage.paste(D, (0,0))
    
    if cell.content == "S":
        baseImage.paste(Start, (0,0), Start)
    elif cell.content == "E":
        baseImage.paste(End, (0,0), End)

    return baseImage