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
        box.label("Rotation")
        row1 = box.row()
        row1.operator("cube_rotate.right")
        row1.operator("cube_rotate.left")
        row2 = box.row()
        row2.operator("cube_rotate.up")
        row2.operator("cube_rotate.down")
        row3 = box.row()
        row3.operator("cube_rotate.front")
        row3.operator("cube_rotate.back")


class OBJECT_OT_AddButton(bpy.types.Operator):

    bl_idname = "cube.add"
    bl_label = "Add"
    mesh = bpy.props.StringProperty()

    def execute(self, context):
        adapter.make_cube()
        return {'FINISHED'}


class CUBE_ROTATE_OT_right(bpy.types.Operator):

    bl_idname = "cube_rotate.right"
    bl_label = "Right"
    mesh = bpy.props.StringProperty()

    def execute(self, context):
        adapter.rotate_cube(enums.Face.right)
        return {'FINISHED'}
class CUBE_ROTATE_OT_left(bpy.types.Operator):

    bl_idname = "cube_rotate.left"
    bl_label = "Left"
    mesh = bpy.props.StringProperty()

    def execute(self, context):
        adapter.rotate_cube(enums.Face.left)
        return {'FINISHED'}
class CUBE_ROTATE_OT_up(bpy.types.Operator):

    bl_idname = "cube_rotate.up"
    bl_label = "Up"
    mesh = bpy.props.StringProperty()

    def execute(self, context):
        adapter.rotate_cube(enums.Face.up)
        return {'FINISHED'}
class CUBE_ROTATE_OT_down(bpy.types.Operator):

    bl_idname = "cube_rotate.down"
    bl_label = "Down"
    mesh = bpy.props.StringProperty()

    def execute(self, context):
        adapter.rotate_cube(enums.Face.down)
        return {'FINISHED'}
class CUBE_ROTATE_OT_back(bpy.types.Operator):

    bl_idname = "cube_rotate.back"
    bl_label = "Back"
    mesh = bpy.props.StringProperty()

    def execute(self, context):
        adapter.rotate_cube(enums.Face.back)
        return {'FINISHED'}
class CUBE_ROTATE_OT_front(bpy.types.Operator):

    bl_idname = "cube_rotate.front"
    bl_label = "Front"
    mesh = bpy.props.StringProperty()

    def execute(self, context):
        adapter.rotate_cube(enums.Face.front)
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
