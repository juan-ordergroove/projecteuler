import math

def divisor_generator(n):
    divisors = {}
    tmp = n
    limit = int(math.sqrt(n))
    for i in range(1, limit+1):
        if tmp % i == 0:
            if i < n: divisors[i] = 1
            if (tmp/i < n): divisors[tmp/i] = 1
    return divisors

def abundants_generator():
    abundants = []
    for n in range(1, 28123):
        div_sum = 0
        divisors = divisor_generator(n)    
        for i in divisors: div_sum += i
        if div_sum > n: abundants.append(n)
    return abundants

def generate_abundant_sums(abundants):
    abundant_sums = {}
    for a in range(len(abundants)):
        for b in range(a, len(abundants)):
            abundant_sums[abundants[a]+abundants[b]] = 1
    return abundant_sums
    
abundants = abundants_generator()
abundant_sums = generate_abundant_sums(abundants)

non_abundant_sum = 0
for i in range(1, 28123):
    if not abundant_sums.get(i): non_abundant_sum += i
print non_abundant_sum
