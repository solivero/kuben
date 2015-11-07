from . import cube, mesher, enums

class BlenderAdapter:

    def __init__(self, bpy):
        self.cube_struct = None
        self.cube_maker = None
        self.bpy = bpy

    def make_cube(self):
        self.cube_struct = cube.Cube()
        self.cube_maker = mesher.CubeMaker(self.bpy)
        self.cube_maker.make_cube(self.cube_struct)
        self.bpy.context.space_data.viewport_shade = "TEXTURED"
        return "Cube Made"

    def rotate_cube(self, face):
        self.cube_struct.rotate_face(face, clockwise=False)
        self.cube_maker.make_cube(self.cube_struct)

