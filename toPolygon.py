def toPolygon(polynomial):
    summed_terms = polynomial.split('+')
    terms = []
    max_xs = 0
    max_ys = 0
    for term in summed_terms:
        subterms = term.split('*')
        
        coeff = float(subterms[0])
        
        xs = 0
        ys = 0

        if len(subterms) > 1:
            for subterm in subterms[1:]:
                if "x" in subterm:
                    xs = xs + 1
                    if "x^" in subterm:
                        xs = xs - 1 + int(subterm.split("^")[1])
                if "y" in subterm:
                    ys = ys + 1
                    if "y^" in subterm:
                        ys = ys - 1 + int(subterm.split("^")[1])
                
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
        polygon[term[2]][term[1]] = term[0]
        
    return(polygon)
