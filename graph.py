import toPolygon
import naiveHull
import findPoints
import twoDHull
import matplotlib.pyplot as plt

def subtract(a,b):
    c = []
    c.append(a[0] - b[0])
    c.append(a[1] - b[1])
    return c

def dot(a,b):
    return a[0] * b[0] + a[1] * b[1]

def graph(polynomial):
    print(toPolygon.toPolygon(polynomial))
    subdivision = naiveHull.naiveHull(toPolygon.toPolygon(polynomial))
    vertices = findPoints.findPoints(subdivision)
    reducedSubdivision = []
    for poly in subdivision:
        reducedSubdivision.append(twoDHull.twoDHull(poly))

    rs = reducedSubdivision
    edges = []
    for p1 in range(0, len(rs)):
        for p2 in range(0, len(rs)):
            if p1 != p2 and (p2,p1) not in edges:
                if any(edge in rs[p2] for edge in rs[p1]):
                    edges.append((p1,p2))
                    
    rays = []
    for vertex in range(0, len(vertices)):
        poly = rs[vertex]
        rayEdges = []
        rayCluster = []
        for edge in poly:
            rayEdge = True
            for other in range(0, len(rs)):
                if rs[other] != poly:
                    if edge in rs[other]:
                        rayEdge = False
            if rayEdge:
                rayEdges.append(edge)
        for ray in rayEdges:
            r = list(ray)
            direction = subtract(r[1],r[0])
            perpendicular = [r[1][1]-r[0][1], -(r[1][0]-r[0][0])]
            for point in subdivision[vertex]:
                if point != r[0] and point != r[1]:
                    if dot(subtract(list(point),r[0]), perpendicular) < 0:
                        perpendicular[0] = -perpendicular[0]
                        perpendicular[1] = -perpendicular[1]
                        break
            rayCluster.append(perpendicular)
        rays.append(rayCluster)

    print(vertices)

    for vertex in vertices:
        plt.scatter(vertex[0], vertex[1], s=5, color='black')
    for edge in edges:
        plt.plot([vertices[edge[0]][0], vertices[edge[1]][0]], [vertices[edge[0]][1], vertices[edge[1]][1]], color='black')
    for rayCluster in range(0, len(rays)):
        for ray in rays[rayCluster]:
            p = vertices[rayCluster]
            plt.arrow(p[0], p[1], ray[0], ray[1], color='black')
    plt.show()
