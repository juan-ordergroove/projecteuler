a = 999
b = 999
max_pal = 0
while a > 0 and b > 0:
    prod = a*b
    if str(prod) == str(prod)[::-1]:
        if prod > max_pal:
            max_pal = prod
    b-=1
    
    if b == 99:
        a -=1
        b = a
print max_pal