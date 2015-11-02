from . import cube, mesher

def make_cube(bpy):
    cube_struct = cube.Cube()
    cube_maker = mesher.CubeMaker(bpy)
    cube_maker.make_cube(cube_struct)
    bpy.context.space_data.viewport_shade = "TEXTURED"
    return "Cube Made"

