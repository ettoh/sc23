import numpy as np
import open3d as o3d
import random

# Flat rectangle with evenly spaced vertices, each displaced by a
# random value between 0 and 1.

GRID_WIDTH = 150
GRID_HEIGHT = 150

# (x, y) coordinates of vertices in the verices array.
# idx | x | y
#  0  | 0 | 0
#  1  | 0 | 1
#  2  | 0 | 2
#  3  | 0 | 3
#  4  | 1 | 0
# ... |...|...
vertices = []

# new vertices at grid position (x,y) with random z coordinates
for x in range(0, GRID_WIDTH):
    for y in range(0, GRID_HEIGHT):
        coord = np.array([x, y, random.uniform(0, 1)])
        vertices.append(coord)

# define faces
triangles = []
for x in range(0, GRID_WIDTH-1):
    for y in range(0, GRID_HEIGHT-1):
        base_idx = x * GRID_WIDTH + y

        # triangle 1
        v0 = base_idx
        v1 = base_idx + GRID_WIDTH
        v2 = base_idx + GRID_WIDTH + 1
        triangles.append(np.array([v0, v1, v2]))

        # triangle 2
        v0 = base_idx + 1
        v1 = base_idx
        v2 = base_idx + GRID_WIDTH + 1
        triangles.append(np.array([v0, v1, v2]))

np_vertices = np.array(vertices)
np_triangles = np.array(triangles)

# Create the mesh
mesh = o3d.geometry.TriangleMesh()
mesh.vertices = o3d.utility.Vector3dVector(np_vertices)
mesh.triangles = o3d.utility.Vector3iVector(np_triangles)

# Save the mesh as an .obj file
o3d.io.write_triangle_mesh("noise.obj", mesh)
