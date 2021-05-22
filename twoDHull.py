import numpy
import itertools

def subtract(a,b):
    c = []
    c.append(a[0] - b[0])
    c.append(a[1] - b[1])
    return c

def dot(a,b):
    return a[0] * b[0] + a[1] * b[1]

def twoDHull(polygon):
    ps = []
    for point in polygon:
        ps.append(point[0:2])

    lines = []
    for element in itertools.combinations(ps, 2):
        if element[0] != element[1]:
            lines.append(element)

    extremes = []
    for line in lines:
        extreme = True
        v = subtract(line[1], line[0])
        v1 = [v[1], -v[0]]
        first = True
        sign = 0
        for point in ps:
            v2 = subtract(point, line[0])
            newSign = numpy.sign(dot(v1,v2))
            if newSign != 0:
                if first:
                    sign = newSign
                    first = False
                else:
                    if newSign != sign:
                        extreme = False
            if newSign == 0:
                if dot(v, v2) > dot(v, v) or dot(v, v2) < 0:
                    extreme = False
        if extreme:
            extremes.append(set([tuple(line[0]), tuple(line[1])]))

    return extremes
