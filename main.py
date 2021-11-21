from game import *


# Rules:
# Any Cell with fewer than 2 live neighbors dies
# Any live cell with two or three live neighbors lives
# Any live cell with more than three live neighbors dies
# Any dead cell with 3 live neighbors becomes live

# Rect(left, top, width, height)

game.game_loop()