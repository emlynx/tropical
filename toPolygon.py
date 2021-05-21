def toPolygon(polynomial):
    summed_terms = polynomial.split('+')
    terms = []
    max_xs = 0
    max_ys = 0
    for term in summed_terms:
        coeff = int(term.split('*')[0])
        
        xs = 0
        if "x" in term:
            xs = 1
            if "x^" in term:
                xs = int(term[term.index("x^") + 2])
        
        ys = 0
        if "y" in term:
            ys = 1
            if "y^" in term:
                ys = int(term[term.index("y^") + 2])
                
        terms.append([coeff, xs, ys])
        if xs > max_xs:
            max_xs = xs
        if ys > max_ys:
            max_ys = ys

    
    polygon = []
    for y in range(0, max_ys + 1):
        polygon.append([])
    for x in range(0, max_xs + 1):
        for row in polygon:
            row.append('i')

    for term in terms:
        print(term)
        polygon[term[2]][term[1]] = term[0]
        
    print(polygon)
