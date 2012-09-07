div_by = [x for x in range(20,1,-1)]
x = 2520
while 1:
    all_div = True
    for i in div_by:
        if x % i != 0:
            all_div = False
            break
    
    if not all_div:
        x += 2520
    else:
        print x
        break