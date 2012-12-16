prod_map = {}
for a in xrange(2, 101):
    for b in xrange(2, 101):
        prod_map[a**b] = True
print len(prod_map)