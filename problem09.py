def pyth_triplet(a,b,c):
    return (a**2 + b**2) == (c**2)

trip_found = False
for a in xrange(500):
    if trip_found: break
    for b in xrange(a+1, 500):
        if trip_found: break
        for c in xrange(b+1, 500):
            if trip_found: break
            if a+b+c != 1000:
                continue

            if pyth_triplet(a,b,c):
                print a,b,c
                print (a*b*c)
                trip_found = True
                break
                