import math
fact_str = str(math.factorial(100))
fact_digit_sum = 0
for i in fact_str:
    fact_digit_sum += int(i)
print fact_digit_sum