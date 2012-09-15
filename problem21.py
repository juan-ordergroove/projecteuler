import math

def divisor_generator(n):
    divisors = []
    tmp = n
    limit = int(math.sqrt(n))
    for i in range(1, limit+1):
        if tmp % i == 0:
            if i < n: divisors.append(i)
            if (tmp/i < n): divisors.append(tmp/i)
    return divisors

def d(n):
    div_sum = 0
    divs = divisor_generator(n)
    for div in divs: div_sum += div
    return div_sum

d_arr = {}
for a in range(10000):
    b = d(a)
    if b == a: continue
    c = d(b)
    
    if c == a: 
        d_arr[a] = 1
        d_arr[b] = 1

d_sum = 0
for i in d_arr:
    d_sum += i
print d_sum