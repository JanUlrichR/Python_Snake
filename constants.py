#Basic Variables for creating and rendering

WIN_HEIGHT = 500
WIN_WIDTH = 500

GAME_DELAY = 50 # ms

BACKGROUND_COLOR = (0,0,0)

#Game Constants

FIELD_SIZE = 50
FIELD_BORDER_SIZE = 1
FIELD_COLOR = (255,255,255)

#Snake Constants

SNAKE_HEAD_COLOR = (0,100,0)
SNAKE_COLOR = (0,255,0)
SNAKE_TO_FIELD_DIFF = 5
SNAKE_SIZE = FIELD_SIZE - 2* SNAKE_TO_FIELD_DIFF

#Apple Constants
APPLE_COLOR = (255,0,0)
APPLE_TO_FIELD_DIFF = 5
APPLE_RADIUS = int(FIELD_SIZE/2 - APPLE_TO_FIELD_DIFF)
