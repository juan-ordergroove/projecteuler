l = 1
n = 1
pivot = 1
diagonal_sum = 1

while l < 1001:
    pivot += 8*n # top right of next level
    diagonal_sum += pivot
    l+=2
    n+=1
    
    j=0
    corner = pivot
    while j < 3:
        corner -= (l-1)
        diagonal_sum += corner
        j+=1
print diagonal_sum