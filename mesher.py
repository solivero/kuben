import bmesh

class CubeMaker:
    def __init__(self, bpy, cublet_radius=1, margin=0.05):
        self.bpy = bpy
        self.cublet_radius = cublet_radius
        self.margin = margin

    def generate_box_points(self, width, height, depth):
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


        verts_loc, faces = self.generate_box_points(1, 1, 1)

        box_mesh = self.get_mesh(verts_loc, faces, repr(cublet.stickers))

        # add the mesh as an object into the scene with this utility module
        from bpy_extras import object_utils
        cube_obj = object_utils.object_data_add(context, box_mesh)
        cube_obj.object.location = [
            coord*(2*self.cublet_radius + self.margin) for coord in (cublet.x, cublet.y, cublet.z)
        ]
        box_mesh.use_paint_mask = True

        #bpy.data.brushes["Draw"].color = (random.random(), random.random(), random.random())
        #bpy.ops.object.mode_set(mode="VERTEX_PAINT")
        #bpy.ops.paint.face_select_all(action='SELECT')
        #bpy.ops.paint.vertex_color_set()

        return {'FINISHED'}

    def make_cube(self, cube):
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
