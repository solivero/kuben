#----------------------------------------------------------
# File __init__.py
#----------------------------------------------------------

#    Addon info
#bl_info = {
#        'name': 'Rubiks Cube',
#        'author': 'Oliver Petri',
#        'location': 'View3D > UI panel > Add meshes',
#        'category': 'Object'
#        }
bl_info = {
        "name": "Rubiks Cube",
        "description": "Creates and animates a Rubik's cube interactivly",
        "author": "Oliver Petri",
        "version": (1, 0),
        "blender": (2, 65, 0),
        "location": "View3D > Add > Mesh",
        "warning": "", # used for warning icon and text in addons panel
        "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.5/Py/"
                    "Scripts/My_Script",
        "category": "Animation"}
# To support reload properly, try to access a package var,
# if it's there, reload everything
if "bpy" in locals():
    import imp
    imp.reload(cube)
    imp.reload(blender)
    imp.reload(enums)
    print("Reloaded multifiles")

else:
    from . import blender, cube, enums
    print("Imported multifiles")

    import bpy
    from bpy.props import *
adapter = blender.BlenderAdapter(bpy)

#
#   class AddMeshPanel(bpy.types.Panel):
#
class AddMeshPanel(bpy.types.Panel):

#
#   class OBJECT_OT_AddButton(bpy.types.Operator):
#
    bl_label = "Cube operations"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    #bl_idname = "OBJECT_PT_select"
    #bl_label = "Select"
    #bl_space_type = 'PROPERTIES'
    #bl_region_type = 'WINDOW'
    #bl_context = "object"
    #bl_options = {'DEFAULT_OPENED'}

    @classmethod
    def poll(cls, context):
        return (context.object is not None)

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        box.label("Clockwise Rotation")
        row1 = box.row()
        row1.operator("cube_rotate.right_cw")
        row1.operator("cube_rotate.left_cw")
        row2 = box.row()
        row2.operator("cube_rotate.up_cw")
        row2.operator("cube_rotate.down_cw")
        row3 = box.row()
        row3.operator("cube_rotate.front_cw")
        row3.operator("cube_rotate.back_cw")

        box = layout.box()
        box.label("Counterclockwise Rotation")
        row1 = box.row()
        row1.operator("cube_rotate.right_ccw")
        row1.operator("cube_rotate.left_ccw")
        row2 = box.row()
        row2.operator("cube_rotate.up_ccw")
        row2.operator("cube_rotate.down_ccw")
        row3 = box.row()
        row3.operator("cube_rotate.front_ccw")
        row3.operator("cube_rotate.back_ccw")


class OBJECT_OT_AddButton(bpy.types.Operator):

    bl_idname = "cube.add"
    bl_label = "Add"
    mesh = bpy.props.StringProperty()

    def execute(self, context):
        adapter.make_cube()
        return {'FINISHED'}


class CUBE_ROTATE_OT_right_ccw(bpy.types.Operator):

    bl_idname = "cube_rotate.right_ccw"
    bl_label = "Right"
    mesh = bpy.props.StringProperty()

    def execute(self, context):
        adapter.rotate_cube(enums.Face.right, clockwise=False)
        return {'FINISHED'}
class CUBE_ROTATE_OT_left_ccw(bpy.types.Operator):

    bl_idname = "cube_rotate.left_ccw"
    bl_label = "Left"
    mesh = bpy.props.StringProperty()

    def execute(self, context):
        adapter.rotate_cube(enums.Face.left, clockwise=False)
        return {'FINISHED'}
class CUBE_ROTATE_OT_up_ccw(bpy.types.Operator):

    bl_idname = "cube_rotate.up_ccw"
    bl_label = "Up"
    mesh = bpy.props.StringProperty()

    def execute(self, context):
        adapter.rotate_cube(enums.Face.up, clockwise=False)
        return {'FINISHED'}
class CUBE_ROTATE_OT_down_ccw(bpy.types.Operator):

    bl_idname = "cube_rotate.down_ccw"
    bl_label = "Down"
    mesh = bpy.props.StringProperty()

    def execute(self, context):
        adapter.rotate_cube(enums.Face.down, clockwise=False)
        return {'FINISHED'}
class CUBE_ROTATE_OT_back_ccw(bpy.types.Operator):

    bl_idname = "cube_rotate.back_ccw"
    bl_label = "Back"
    mesh = bpy.props.StringProperty()

    def execute(self, context):
        adapter.rotate_cube(enums.Face.back, clockwise=False)
        return {'FINISHED'}
class CUBE_ROTATE_OT_front_ccw(bpy.types.Operator):

    bl_idname = "cube_rotate.front_ccw"
    bl_label = "Front"
    mesh = bpy.props.StringProperty()

    def execute(self, context):
        adapter.rotate_cube(enums.Face.front, clockwise=False)
        return {'FINISHED'}
## CLOCKWISE STARTS HERE
class CUBE_ROTATE_OT_right_cw(bpy.types.Operator):

    bl_idname = "cube_rotate.right_cw"
    bl_label = "Right"
    mesh = bpy.props.StringProperty()

    def execute(self, context):
        adapter.rotate_cube(enums.Face.right, clockwise=True)
        return {'FINISHED'}
class CUBE_ROTATE_OT_left_cw(bpy.types.Operator):

    bl_idname = "cube_rotate.left_cw"
    bl_label = "Left"
    mesh = bpy.props.StringProperty()

    def execute(self, context):
        adapter.rotate_cube(enums.Face.left, clockwise=True)
        return {'FINISHED'}
class CUBE_ROTATE_OT_up_cw(bpy.types.Operator):

    bl_idname = "cube_rotate.up_cw"
    bl_label = "Up"
    mesh = bpy.props.StringProperty()

    def execute(self, context):
        adapter.rotate_cube(enums.Face.up, clockwise=True)
        return {'FINISHED'}
class CUBE_ROTATE_OT_down_cw(bpy.types.Operator):

    bl_idname = "cube_rotate.down_cw"
    bl_label = "Down"
    mesh = bpy.props.StringProperty()

    def execute(self, context):
        adapter.rotate_cube(enums.Face.down, clockwise=True)
        return {'FINISHED'}
class CUBE_ROTATE_OT_back_cw(bpy.types.Operator):

    bl_idname = "cube_rotate.back_cw"
    bl_label = "Back"
    mesh = bpy.props.StringProperty()

    def execute(self, context):
        adapter.rotate_cube(enums.Face.back, clockwise=True)
        return {'FINISHED'}
class CUBE_ROTATE_OT_front_cw(bpy.types.Operator):

    bl_idname = "cube_rotate.front_cw"
    bl_label = "Front"
    mesh = bpy.props.StringProperty()

    def execute(self, context):
        adapter.rotate_cube(enums.Face.front, clockwise=True)
        return {'FINISHED'}

#
#    Registration
#
def add_cube_mesh(self, context):
    self.layout.operator("cube.add", text="Add cube", icon="MESH_CUBE").mesh = "cube"

def register():
    print("Trying to register")
    bpy.utils.register_module(__name__, verbose=True)
    bpy.types.INFO_MT_add.append(add_cube_mesh)

def unregister():
    bpy.utils.unregister_module(__name__, verbose=True)

if __name__ == "__main__":
    register()
    print("Registered")
