def find_reps(dec):
    d_mid = len(dec)/2
    for i in xrange(len(dec)-1, d_mid, -1):
        sub = dec[i:]
        new_dec = dec[:len(dec)-len(sub)]
        print new_dec, sub
        if new_dec.find(sub) != -1: return len(sub)
    return 0

def div(d):
    m = 1
    dec = ''
    while m != 0:
        p = int(str(m)+str('0'))
        n = p/d
        dec += str(n)
        m = p - (n*d)

        curr_reps = find_reps(dec)
        if curr_reps != 0: return curr_reps
    return 0

reps = div(14)
print reps
# d = 2
# reps = 0
# while d < 1000:
#     new_reps = div(d)
#     if new_reps > reps:
#         reps = new_reps
#         max_d = d
#     d+=1
# print max_d, reps