from SpriteSheet import *
import sys, os

# Game Settings

script_dir = sys.path[0]
img_path = os.path.join(script_dir, 'Game Boy Advance - Pokemon Emerald - Brendan.PNG')

FPS = 60
MAIN_MALE_CHARACTER = SpriteSheet(img_path
