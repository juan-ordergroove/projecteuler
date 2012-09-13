# Sovled by Chris DuBois
# Coded by Juan Gutierrez
import sys, math

def generate_points():
    print 'p: n/2=',(n/2)
    for p in range((n/2)-1, 0, -1):
        print 'p:',p
        x.append(1 - (2 * (sine_p(p) ** 2)))
        y.append(2 * sine_p(p) * cose_p(p))
    print 'p: 0'
    x.append(1)
    y.append(0)

def sine_p(p):
    return math.sin((p*math.pi)/(2*n))

def cose_p(p):
    return math.cos((p*math.pi)/(2*n))

def generate_sum():
    rect_sum = 0
    print '\n'
    for j in range(0, (n/2)):
        print 'j:',j
        rect_sum += (x[j+1] * (y[j] - y[j+1]))
    return rect_sum*4
    
if __name__ == '__main__':
    if len(sys.argv) == 1: print 'you idiot! you must define N!'
    
    try: N = int(sys.argv[1])
    except: N = 1

    if N % 2 != 0: n = N + 1
    else: n = N
    
    print 'n:', n

    x = [0]
    y = [1]

    generate_points()
    print '\n'
    print 'x'
    print x
    print '\n'
    print 'y'
    print y
    print generate_sum()

