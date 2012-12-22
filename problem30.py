class DigitPower(object):

    power = 0
    power_map = []
    sum_dict = {}
    
    def __init__(self, power):
        self.power = power
        for i in xrange(0, 10): self.power_map.append(i**self.power)
        print self.power_map

    def scan_sum(self, digits):
        idx_list = []
        exp_sum = 0
        for d in digits: exp_sum += self.power_map[int(d)]
        exp_sum = str(exp_sum)

        if len(exp_sum) == 1: return False
        return True if str(exp_sum) == str(digits) else False

    def digit_itr(self, digits, depth):

        if depth == self.power+2: return
        for d in xrange(0, 10):
            new_digits = digits+str(d)
            self.digit_itr(new_digits, depth+1)
            if self.scan_sum(new_digits): 
                self.sum_dict[new_digits] = True

    def init(self):
        for a in xrange(0, 10): self.digit_itr(str(a), 1)

sum_dict = {}
dp = DigitPower(5)
dp.init()
print dp.sum_dict
