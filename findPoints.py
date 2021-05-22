from numpy.linalg import inv
import numpy as np

def findPoints(subdivision):
    vertices = []
    for poly in subdivision:
        p = poly[0]
        q = poly[1]
        r = poly[2]

        a = np.matrix([[p[0], p[1], -1], [q[0], q[1], -1], [r[0], r[1],-1]])
        ainv = inv(a)

        b = np.array([-p[2], -q[2], -r[2]])

        vertex = ainv.dot(b).tolist()

        vertices.append(vertex[0][0:2])
    return vertices
