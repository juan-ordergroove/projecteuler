import math

triangle_number = 1
triangle_idx = 1
divisors = []

while len(divisors) <= 500:

    triangle_idx+=1
    triangle_number+=triangle_idx
    divisors = []
    
    n = int(math.sqrt(triangle_number))
    tmp = triangle_number
    for i in range(1,n+1):
        if tmp % i == 0: 
            divisors.append(i)
            divisors.append(tmp/i)
print triangle_number, divisors