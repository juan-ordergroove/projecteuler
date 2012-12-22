class CoinSums(object):

    coin_sum = 1 # there is a 200p coin = 2pounds
    coins = [100,50,20,10,5,2,1]
    
    def coin_counter(self, coin_idx, current_sum):
        if current_sum == 200:
            self.coin_sum +=1
            return
        elif current_sum > 200: return
        
        for c_idx in xrange(coin_idx, len(self.coins)):
            self.coin_counter(c_idx, current_sum+self.coins[c_idx])
        
    def init(self):
        coin_idx = 0
        for c_idx in xrange(0, len(self.coins)):
            self.coin_counter(c_idx, self.coins[c_idx])

cs = CoinSums()
cs.init()
print cs.coin_sum