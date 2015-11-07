import bmesh
import random
from .enums import Color

class CubeMaker:
    def __init__(self, bpy, cublet_radius=1, margin=0.05):
        self.bpy = bpy
        self.cublet_radius = cublet_radius
        self.margin = margin
        self.cube = [[[[] for i in range(3)] for i in range(3)] for k in range(3)]

    def generate_box_points(self, width, depth, height):
        """
        This function takes inputs and returns vertex and face arrays.
        no actual mesh data creation is done here.
        """

        verts = [(+1.0, +1.0, -1.0),
                (+1.0, -1.0, -1.0),
                (-1.0, -1.0, -1.0),
                (-1.0, +1.0, -1.0),
                (+1.0, +1.0, +1.0),
                (+1.0, -1.0, +1.0),
                (-1.0, -1.0, +1.0),
                (-1.0, +1.0, +1.0),
                ]

        faces = [(0, 1, 2, 3),
                (4, 7, 6, 5),
                (0, 4, 5, 1),
                (1, 5, 6, 2),
                (2, 6, 7, 3),
                (4, 0, 3, 7),
                ]

        # apply size
        for i, v in enumerate(verts):
            verts[i] = v[0] * width, v[1] * depth, v[2] * height

        return verts, faces

    def make_cublet(self, context, cublet):

        from bpy_extras import object_utils

        verts_loc, faces = self.generate_box_points(1, 1, 1)
        box_mesh = self.get_mesh(verts_loc, faces, repr(cublet))
        self.color_mesh(box_mesh, (0.05, 0.05, 0.05))

        # add the mesh as an object into the scene with this utility module
        cube_obj = object_utils.object_data_add(context, box_mesh)
        cube_obj.object.location = [
            coord*(2*self.cublet_radius + self.margin) for coord in (cublet.x, cublet.y, cublet.z)
        ]

        for sticker in cublet.stickers:
            dimensions = [0, 0, 0]
            location = [0, 0, 0]
            #cubl_xyz = [cublet.x, cublet.y, cublet.z]
            for i, val in enumerate(sticker['face'].value):
                # Use for absolute position, comment for relative position to cublet
                #location[i] = cubl_xyz[i]*(2*self.cublet_radius + self.margin)
                if val != 0:
                    dimensions[i] = 0.02
                    location[i] += val*1.02
                else:
                    dimensions[i] = 0.9
                #print("{} {} {}".format(i, val, dimensions))

            verts_loc, faces = self.generate_box_points(*dimensions)
            sticker_mesh = self.get_mesh(verts_loc, faces, repr(sticker))

            self.color_mesh(sticker_mesh, sticker['color'])

            sticker_obj = object_utils.object_data_add(context, sticker_mesh)
            sticker_obj.object.location = location
            sticker_obj.object.parent = cube_obj.object

        self.cube[cublet.x+1][cublet.y+1][cublet.z+1] = cube_obj
        return {'FINISHED'}

    def color_mesh(self, mesh, color):
        if type(color) != tuple:
            table = {
                Color.white:    (1, 1, 1),
                Color.yellow:   (0.8, 0.8, 0),
                Color.blue:     (0.2, 0.2, 1),
                Color.green:    (0.3, 1, 0),
                Color.red:      (0.9, 0, 0),
                Color.orange:   (1, 0.7, 0),
            }
            color = table[color]
        color_map_collection = mesh.vertex_colors
        if len(color_map_collection) == 0:
            color_map = color_map_collection.new()

        for layer in mesh.vertex_colors:
            layer.active = True
            layer.active_render = True
            for loop_color in layer.data:
                loop_color.color = color

        mat = self.bpy.data.materials.new('vertex_material')
        mat.use_vertex_color_paint = True
        mat.use_vertex_color_light = True  # material affected by lights

        mesh.materials.append(mat)

    def make_cube(self, cube):
        #for x in self.cube:
        #    for y in x:
        #        for obj in y:
        #            if type(obj) != list:
        #                for child in obj.object.children:
        #                    self.bpy.data.objects.remove(child)
        #                self.bpy.data.objects.remove(obj)

        self.bpy.ops.object.select_all(action='SELECT')
        self.bpy.ops.object.delete()
        for x_axis in cube.cublets:
            for y_axis in x_axis:
                for cublet in y_axis:
                    self.make_cublet(self.bpy.context, cublet)

    def keyframe(self, name):
        obj = self.bpy.data.objects[name]

        # set the keyframe at frame 1
        obj.location = 3.0, 4.0, 10.0
        obj.keyframe_insert(data_path="location", frame=1)

    def get_mesh(self, verts_loc, faces, name="cubemesh"):
        mesh = self.bpy.data.meshes.new(name)

        bm = bmesh.new()

        for v_co in verts_loc:
            bm.verts.new(v_co)

        bm.verts.ensure_lookup_table()
        for f_idx in faces:
            bm.faces.new([bm.verts[i] for i in f_idx])

        bm.to_mesh(mesh)
        mesh.update()
        return mesh


#keyframe("Box")
