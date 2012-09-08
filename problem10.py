import math
primes = [2]
n = 3
while 1:
    p_found = True
    limit = math.sqrt(n)
    for p in primes:
        if p <= limit:
            if n%p == 0:
                p_found = False
                break
        else:
            break
    
    if p_found:
        primes.append(n)
    n += 2
    if n % 1000 == 0: print '-'
    if n >= 2000000: break

p_sum = 0
for p in primes:
    p_sum += p
print primes
print p_sum

