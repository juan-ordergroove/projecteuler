import math
n = 600851475143
limit = int(math.sqrt(n))
factors = []
d = 2
while n > 1:
    if (n%d == 0):
        factors.append(d)
        n /= d
        print n, factors
    d = d+1
print factors