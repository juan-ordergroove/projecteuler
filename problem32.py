import itertools

class PanDigitalProducts(object):

    products = []
    series_lim = 9

    def __init__(self):
        self.perms = itertools.permutations([1,2,3,4,5,6,7,8,9])
        for p in self.perms:
            print p
            self.check_products(p)
        print self.products

    def check_products(self, digits):
        floating_idx = 1
        floating_len = 1
        product_valid = True
        for i in xrange(1, self.series_lim-1):
            for j in xrange(i+1, self.series_lim-2):
                multiplicand = self.gen_num(digits, 0, i)
                multiplier = self.gen_num(digits, i, j)
                product = self.gen_num(digits, j, self.series_lim)

                if len(str(product)) > self.series_lim: break

                product_match = (multiplicand*multiplier)==product
                if product_match and product not in self.products: self.products.append(product)

    def gen_num(self, digits, n, m):
        i=n
        num = ''
        while i < m:
            num += str(digits[i])
            i+=1
        return int(num)

p = PanDigitalProducts()
