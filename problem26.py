def x(d, reps):
    m = 1
    dec = ''
    while m != 0:
        p = int(str(m)+str('0'))
        n = p/d
        d_mid = len(dec)/2        

        ldm = (dec and str(n) == dec[-1]) # last digit matches
        if ldm: return 1

        dec += str(n)
        # print '0.'+dec
        m = p - (n*d)

        for i in xrange(len(dec)-reps-1, d_mid, -1):
            sub = dec[len(dec)-reps-1:]
            new_dec = dec[:len(dec)-reps-1]
            print reps, sub, new_dec
            if new_dec.find(sub) != -1: return i-1
    return 0

d = 2
reps = 0
# reps = max(x(14, reps), reps)
# print reps
while d < 1000:
    new_reps = x(d, reps)
    if new_reps > reps:
        reps = new_reps
        max_d = d
    d+=1
print max_d, reps