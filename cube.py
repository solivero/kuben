from math import sin, cos, radians
import copy

from .enums import Color, Face


class Cublet:
    def __repr__(self):
        return "x:{} y:{} z:{} \ncolors:{}".format(
            self.x,
            self.y,
            self.z,
            self.stickers
        )

    def __init__(self, x, y, z, stickers):
        self.x = x
        self.y = y
        self.z = z
        self.stickers = stickers


class Cube:
    def __repr__(self):
        return repr(self.cublets)

    def rotate_cublet_x(self, cublet):
        # 90 deg == counter clockwise
        # not needed as sin(90)=1 and cos(90)=0
        # theta = radians(theta)
        # sin_t = sin(theta)
        # cos_t = cos(theta)
        new_cublet = copy.deepcopy(cublet)
        new_cublet.z = -cublet.y
        new_cublet.y = cublet.z
        #print("X: {} -> {}".format((cublet.x, cublet.y, cublet.z,), (new_cublet.x, new_cublet.y, new_cublet.z)))
        for i in range(len(cublet.stickers)):
            face = cublet.stickers[i]['face'].value
            x, y, z = face
            new_cublet.stickers[i]['face'] = Face((x, z, -y))
        return new_cublet

    def rotate_cublet_y(self, cublet):
        new_cublet = copy.deepcopy(cublet)
        new_cublet.x = -cublet.z
        new_cublet.z = cublet.x
        #print("Y: {} -> {}".format((cublet.x, cublet.y, cublet.z,), (new_cublet.x, new_cublet.y, new_cublet.z)))
        for i in range(len(cublet.stickers)):
            face = cublet.stickers[i]['face'].value
            x, y, z = face
            new_cublet.stickers[i]['face'] = Face((-z, y, x))
        return new_cublet

    def rotate_cublet_z(self, cublet):
        new_cublet = copy.deepcopy(cublet)
        new_cublet.x = -cublet.y
        new_cublet.y = cublet.x
        #print("Z: {} -> {}".format((cublet.x, cublet.y, cublet.z,), (new_cublet.x, new_cublet.y, new_cublet.z)))
        for i in range(len(cublet.stickers)):
            face = cublet.stickers[i]['face'].value
            x, y, z = face
            new_cublet.stickers[i]['face'] = Face((-y, x, z))
        return new_cublet

    def rotate_face(self, face, clockwise):
        if clockwise:
            p = 3
            q = 1
        else:
            p = 1
            q = 3

        new_face = []
        if face is Face.up:
            for i in range(p):
                for x in range(3):
                    for y in range(3):
                        new_face.append(self.rotate_cublet_z(self.cublets[x][y][2]))
                for cublet in new_face:
                    self.cublets[cublet.x+1][cublet.y+1][cublet.z+1] = cublet
        elif face is Face.down:
            for i in range(q):
                for x in range(3):
                    for y in range(3):
                        new_face.append(self.rotate_cublet_z(self.cublets[x][y][0]))
                for cublet in new_face:
                    self.cublets[cublet.x+1][cublet.y+1][cublet.z+1] = cublet
        elif face is Face.left:
            for i in range(p):
                for y in range(3):
                    for z in range(3):
                        new_face.append(self.rotate_cublet_x(self.cublets[0][y][z]))
                for cublet in new_face:
                    self.cublets[cublet.x+1][cublet.y+1][cublet.z+1] = cublet
        elif face is Face.right:
            for i in range(q):
                for y in range(3):
                    for z in range(3):
                        new_face.append(self.rotate_cublet_x(self.cublets[2][y][z]))
                for cublet in new_face:
                    self.cublets[cublet.x+1][cublet.y+1][cublet.z+1] = cublet

        elif face is Face.back:
            for i in range(q):
                for x in range(3):
                    for z in range(3):
                        new_face.append(self.rotate_cublet_y(self.cublets[x][2][z]))
                for cublet in new_face:
                    self.cublets[cublet.x+1][cublet.y+1][cublet.z+1] = cublet
        elif face is Face.front:
            for i in range(p):
                for x in range(3):
                    for z in range(3):
                        new_face.append(self.rotate_cublet_y(self.cublets[x][0][z]))
                for cublet in new_face:
                    self.cublets[cublet.x+1][cublet.y+1][cublet.z+1] = cublet

    def rotate_cube(self, clockwise):
        if clockwise:
            n = 3
        else:
            n = 1
        for column in self.cublets:
            for depth in column:
                for cublet in depth:
                    for i in range(n):
                        cublet = self.rotate_cublet_z(cublet)

    def flip_cube(self):
        for i in range(2):
            for column in self.cublets:
                for depth in column:
                    for cublet in depth:
                        cublet = self.rotate_cublet_x(cublet)

    def __init__(self):

    # X(left(red)-right(orange)) Y(front(blue)-back(green)) Z (down(yellow)-up(white))
        color_to_face = {
            Color.red: Face.left,
            Color.orange: Face.right,
            Color.blue: Face.front,
            Color.green: Face.back,
            Color.yellow: Face.down,
            Color.white: Face.up
        }
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
                                stickers.append(
                                    {'color': color,
                                     'face': color_to_face[color]}
                                )
                                break
                    self.cublets[x][y][z] = Cublet(x-1, y-1, z-1, stickers)


if __name__ == '__main__':
    cube = Cube()
    print(cube.cublets)
    cube.rotate_face(Face.up, clockwise=True)
    print("ROTATED")
    print(cube)
