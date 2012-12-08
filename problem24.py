''' First 20 output by BruteLexicographicItr:
123456789 1
123456798 2
123456879 3
123456897 4
123456978 5
123456987 6
123457689 7
123457698 8
123457869 9
123457896 10
123457968 11
123457986 12
123458679 13
123458697 14
123458769 15
123458796 16
123458967 17
123458976 18
123459678 19
123459687 20'''


# class BruteLexicographicItr(object):
#     
#     def __init__(self, lexicographic_limit):
# 
#         self.lexi_count = 0
#         self.num = 123456789
#         self.digits_arr = [0,1,2,3,4,5,6,7,8,9]
#         self.lexicographic_limit = lexicographic_limit
#     
#     def itr(self):
#         
#         while self.lexi_count < self.lexicographic_limit:
#             b_contains_digits = True
#             for i in self.digits_arr:
#                 if i == 0 and self.num < 1000000000: continue
#                 if str(i) not in str(self.num):
#                     b_contains_digits = False
#                     break
#             
#             if b_contains_digits:
#                 self.lexi_count += 1
#                 print self.num, self.lexi_count
#             self.num += 1
# 
# if __name__ == '__main__':
#     bli = BruteLexicographicItr(10**6)
#     bli.itr()
