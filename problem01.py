multi_sum = 0
for i in xrange(1000):
    if (i % 3) == 0 or (i % 5) == 0:
        multi_sum += i
print multi_sum