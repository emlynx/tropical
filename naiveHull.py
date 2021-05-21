import itertools

def cross(a,b):
    c = []
    c.append(a[1]*b[2]-a[2]*b[1])
    c.append(a[2]*b[0]-a[0]*b[2])
    c.append(a[0]*b[1]-a[1]*b[0])
    return c

def positiveCross(a,b):
    c = cross(a,b)
    if c[2] < 0:
        c[0] = -c[0]
        c[1] = -c[1]
        c[2] = -c[2]
    return c

def unitize(a):
    length = (a[0] ** 2 + a[1] ** 2 + a[2] ** 2) ** (1/2)
    u = []
    if length != 0:
        u.append(a[0]/length)
        u.append(a[1]/length)
        u.append(a[2]/length)
    else:
        u = a
    return u

def subtract(a,b):
    c = []
    c.append(a[0] - b[0])
    c.append(a[1] - b[1])
    c.append(a[2] - b[2])
    return c

def dot(a,b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def naiveHull(polygon):
    ps = []
    for y in range(0, len(polygon)):
        for x in range(0, len(polygon[0])):
            if polygon[y][x] != 'i':
                ps.append([x, y, polygon[y][x]])

    triads = []
    for element in itertools.combinations(ps, 3):
        if element[0] != element[1] and element[0] != element[2] and element[1] != element[2]:
            triads.append(element)

    hull = []
    for triad in triads:
        v1 = subtract(triad[0], triad[1])
        v2 = subtract(triad[0], triad[2])
        upwardsNormal = unitize(positiveCross(v1,v2))
        if upwardsNormal[2] != 0:
            onHull = True
            for p in ps:
                v3 = subtract(p, triad[0])
                if dot(v3, upwardsNormal) < 0:
                    onHull = False
            if onHull:
                hull.append([list(triad), upwardsNormal])

    blah = True
    while blah:
        blah = False
        for m in range(0, len(hull)):
            for n in range(m, len(hull)):
                if len([x for x in hull[m][0] if x in hull[n][0]]) >= 2 and m != n and hull[m][1] == hull[n][1]:
                    blah = True
                    hull[m] = [list(map(list, set(map(tuple, hull[m][0] + hull[n][0])))), hull[m][1]]
                    hull.remove(hull[n])
                    break
    for x in hull:
        print(x)
    print(len(hull))
