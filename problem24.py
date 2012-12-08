''' First 20 output:
0123456789 1
0123456798 2
0123456879 3
0123456897 4
0123456978 5
0123456987 6
0123457689 7
0123457698 8
0123457869 9
0123457896 10
0123457968 11
0123457986 12
0123458679 13
0123458697 14
0123458769 15
0123458796 16
0123458967 17
0123458976 18
0123459678 19
0123459687 20
'''

import copy
class TreeLexiCounter(object):
    
    def __init__(self, lex_limit):
        self.solution = None
        self.p_counter = 0
        self.lex_limit = lex_limit
        self.digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.d_limit = len(self.digits)
    
    def _itr(self, d_pos, used_digits):
        
        if d_pos == self.d_limit: self.p_counter+=1
        if not self.solution and self.p_counter >= self.lex_limit:
            self.solution = copy.deepcopy(used_digits)
            return
        
        for d in self.digits:
            if self.solution: return
            if d in used_digits: continue

            used_digits.append(d)
            self._itr(d_pos+1, used_digits)
            used_digits.remove(d)
    
    def start(self):
        d_pos = 0
        used_digits = []
        self._itr(d_pos, used_digits)

if __name__ == '__main__':
    tlc = TreeLexiCounter(10**6)
    tlc.start()
    print tlc.solution
