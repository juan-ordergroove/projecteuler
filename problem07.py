primes = [2,3,5,7,11,13]
n = 17
while 1:
    p_found = True
    for p in primes:
        if n%p == 0:
            p_found = False
            break
    
    if p_found:
        primes.append(n)
        if len(primes) == 10001:
            break
    n += 2
print primes[len(primes)-1]