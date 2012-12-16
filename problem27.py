import math
coef_max = 1000
prime_map = []

def is_prime(x):
    for i in xrange(2, int(math.sqrt(x))+1):
        if x%i == 0: return False
    return True

def quad(a, b):
    n = 0
    while 1:
        x = int(math.fabs((n**2) + (a*n) + b))

        if not x: return n
        if x in prime_map: n+=1
        elif is_prime(x):
            n+=1
            prime_map.append(x) 
        else: return n

n_max = 0
coef_prod = 0
for a in xrange(coef_max*(-1), coef_max):
    print "a:",a
    for b in xrange(coef_max*(-1), coef_max):
        n = quad(a, b)
        if n > n_max:
            n_max = n
            coef_prod = a*b
print n_max, coef_prod