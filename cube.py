from enum import Enum
from copy import deepcopy
from math import sin, cos, radians
class Face(Enum):
    up = 1
    down = 2
    front = 3
    back = 4
    left = 5
    right = 6

class Color(Enum):
    white = 1
    yellow = 2
    blue = 3
    green = 4
    red = 5
    orange = 6

class Cublet:
    def __repr__(self):
        return "x:{} y:{} z:{} colors:{}\n".format(self.x, self.y, self.z, self.stickers)

    def __init__(self, x, y, z, stickers):
        self.x = x
        self.y = y
        self.z = z
        self.stickers = stickers

class Cube:
    def __repr__(self):
        return self.cublets

    def rotate_cube(self, theta):
        theta = radians(theta)
        sin_t = sin(theta)
        cos_t = cos(theta)
        if theta == 90:
            sin_t = int(sin_t)
            cos_t = int(cos_t)

        for row in self.cublets:
            for depth in row:
                for cublet in depth:
                    x = cublet.x
                    y = cublet.y
                    cublet.x = x * cos_t - y * sin_t
                    cublet.y = y * cos_t + x * sin_t
    def __init__(self):

    ### X(left(red)-right(orange)) Y(front(blue)-back(green)) Z (down(yellow)-up(white))
        self.cublets = [
            [
                ["rby", "rb", "rbw"],
                ["ry", "r", "rw"],
                ["ryg", "rg", "rgw"]
            ],
            [
                ["by", "b", "bw"],
                ["y", "", "w"],
                ["gy", "g", "gw"]
            ],
            [
                ["oby", "ob", "obw"],
                ["oy", "o", "ow"],
                ["ogy", "og", "ogw"]
            ]
        ]

        for x in range(3):
            for y in range(3):
                for z in range(3):
                    stickers = []
                    for letter in self.cublets[x][y][z]:
                        for color in Color:
                            if color.name[0] == letter:
                                stickers.append((color, Face(color.value)))
                                break
                    self.cublets[x][y][z] = (Cublet(x-1, y-1, z-1, stickers))


if __name__ == '__main__':
    cube = Cube()
    print(cube.cublets)
    cube.rotate_cube(90)
    print("ROTATED")
    print(cube.cublets)
