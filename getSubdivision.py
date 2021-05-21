def getSubdivision(polygon):
    first = True
    least_coeff = ['i', 0, 0]
    for ys in range(0, len(polygon)):
        for xs in range(0, len(polygon[0])):
            if first == True:
                if polygon[ys][xs] != 'i':
                    least_coeff = [polygon[ys][xs], xs, ys]
                    first = False
            else:
                if polygon[ys][xs] != 'i':
                    if polygon[ys][xs] <= least_coeff[0]:
                        least_coeff = [polygon[ys][xs], xs, ys]

    first = True
    least_slope = 'i'
    least_slope_coord = ['i',0,0]
    for ys in range(0, len(polygon)):
        for xs in range(0, len(polygon[0])):
            if (xs, ys) != (least_coeff[1], least_coeff[2]):
                if first == True:
                    if polygon[ys][xs] != 'i':
                        dc = polygon[ys][xs] - least_coeff[0]
                        dx = xs - least_coeff[2]
                        dy = ys - least_coeff[1]
                        dist = (dx ** 2 + dy ** 2) ** (1/2)
                        print(dx, dy, dc/dist)
                        least_slope = dc/dist
                        least_slope_coord = [polygon[ys][xs], xs, ys]
                        first = False
                else:
                    if polygon[ys][xs] != 'i':
                        dc = polygon[ys][xs] - least_coeff[0]
                        dx = xs - least_coeff[2]
                        dy = ys - least_coeff[1]
                        dist = (dx ** 2 + dy ** 2) ** (1/2)
                        print(dx, dy, dc/dist)
                        if dc/dist < least_slope:
                            least_slope = dc/dist
                            least_slope_coord = [polygon[ys][xs], xs, ys]

    print(least_coeff)
    print(least_slope_coord)
