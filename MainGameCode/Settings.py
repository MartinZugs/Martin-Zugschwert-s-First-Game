from SpriteSheet import *
import sys, os
import pygame as pg

# Game Settings
pg.init()

# Display Variables
WIDTH, HEIGHT = 500, 500
HW, HH = WIDTH/2, HEIGHT/2
AREA = WIDTH * HEIGHT
TITLE = "Pokemon Game"

# Colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

script_dir = sys.path[0]
wleft = pg.image.load(os.path.join(script_dir, 'Game Boy Advance - Pokemon Emerald - BrendanWalkingLeft.PNG'))
wright = pg.image.load(os.path.join(script_dir, 'Game Boy Advance - Pokemon Emerald - BrendanWalkingRight.PNG'))
wdown = pg.image.load(os.path.join(script_dir, 'Game Boy Advance - Pokemon Emerald - BrendanWalkingDown.PNG'))
wup = pg.image.load(os.path.join(script_dir, 'Game Boy Advance - Pokemon Emerald - BrendanWalkingUp.PNG'))
pwoods = pg.image.load(os.path.join(script_dir, "Game Boy Advance - Pokemon Emerald - PetalburgWoodsScaled.PNG"))

FPS = 60

MAIN_MALE_CHARACTER_WALKING_LEFT = SpriteSheet(wleft, 1, 3)
MAIN_MALE_CHARACTER_WALKING_RIGHT = SpriteSheet(wright, 1, 3)
MAIN_MALE_CHARACTER_WALKING_DOWN = SpriteSheet(wdown, 1, 3)
MAIN_MALE_CHARACTER_WALKING_UP = SpriteSheet(wup, 1, 3)
