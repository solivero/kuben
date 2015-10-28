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

#
#   class AddMeshPanel(bpy.types.Panel):
#
class AddMeshPanel(bpy.types.Panel):
    bl_label = "Add meshes"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    def draw(self, context):
        self.layout.operator("cube.add", text="Add cube").mesh = "cube"

#
#   class OBJECT_OT_AddButton(bpy.types.Operator):
#
class OBJECT_OT_AddButton(bpy.types.Operator):
    bl_idname = "cube.add"
    bl_label = "Add"
    mesh = bpy.props.StringProperty()
    def execute(self, context):
        blender.make_cube(bpy)
        return {'FINISHED'}
#
#    Registration
#

def register():
    print("Trying to register")
    bpy.utils.register_module(__name__, verbose=True)

def unregister():
    bpy.utils.unregister_module(__name__, verbose=True)

if __name__ == "__main__":
    register()
    print("Registered")
