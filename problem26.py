def x(d):
    m = 1
    dec = ''
    while m != 0:
        p = int(str(m)+str('0'))
        n = p/d
        d_mid = len(dec)/2        

        ldm = (dec and str(n) == dec[-1]) # last digit matches
        first_part, second_part = dec[:d_mid], dec[d_mid:]        

        if ldm: return 1
        elif (dec and first_part == second_part): return len(first_part)

        dec += str(n)
        print '0.'+dec
        m = p - (n*d)
    return 0

d = 2
reps = 0
x(14)
# while d < 1000:
#     reps = max(x(d), reps)
#     d+=1
# print reps