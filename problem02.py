i = 1
prev_i = 1
limit = 4*(10**6)
even_sum = 0
while i < limit:
    if (i % 2) == 0:
        even_sum += i
    tmp = i
    i += prev_i
    prev_i = tmp
print even_sum