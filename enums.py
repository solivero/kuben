from enum import Enum

class Face(Enum):
    up = (0, 0, 1)
    down = (0, 0, -1)
    front = (0, -1, 0)
    back = (0, 1, 0)
    left = (-1, 0, 0)
    right = (1, 0, 0)

class Color(Enum):
    white = 1
    yellow = 2
    blue = 3
    green = 4
    red = 5
    orange = 6
