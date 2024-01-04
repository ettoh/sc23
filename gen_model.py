import numpy as np
import open3d as o3d
import random

width = 150
height = 150
vertices = []
triangles = []

# idx | x | y
#  0  | 0 | 0
#  1  | 0 | 1
#  2  | 0 | 2
#  3  | 0 | 3
#  4  | 1 | 0
#  .  | . | .

# create height at each grid posititons
for x in range(0, width):
    for y in range(0, height):
        coord = np.array([x, y, random.uniform(0, 1)])
        vertices.append(coord)

# define faces
for x in range(0, width-1):
    for y in range(0, height-1):
        base_idx = x * width + y

        # triangle 1
        v0 = base_idx
        v1 = base_idx + width
        v2 = base_idx + width + 1
        triangles.append(np.array([v0, v1, v2]))

        # triangle 2
        v0 = base_idx + 1
        v1 = base_idx
        v2 = base_idx + width + 1
        triangles.append(np.array([v0, v1, v2]))

np_vertices = np.array(vertices)
np_triangles = np.array(triangles)

# Create a mesh
mesh = o3d.geometry.TriangleMesh()
mesh.vertices = o3d.utility.Vector3dVector(np_vertices)
mesh.triangles = o3d.utility.Vector3iVector(np_triangles)

# Save the mesh as an .obj file
o3d.io.write_triangle_mesh("noise.obj", mesh)
