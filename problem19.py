# Months go from 0 to 11
# Days of the week:
# 0: sunday
# 1: monday
# 2: tuesday
# 3: wednesday
# 4: thursday
# 5: friday
# 6: saturday

class SundayCounter(object):
    
    week_day = 1
    month = 0
    day = 1
    year = 1900
    sunday_counter = 0
    month_days = {
        0: 31,  #  1 - 31
        1: 28,  #  2 - 28 except leap
        2: 31,  #  3 - 31
        3: 30,  #  4 - 30
        4: 31,  #  5 - 31
        5: 30,  #  6 - 30
        6: 31,  #  7 - 31
        7: 31,  #  8 - 31
        8: 30,  #  9 - 30
        9: 31,  # 10 - 31
        10: 30, # 11 - 30
        11: 31  # 12 - 31
        }

    def traverse_months(self, count_sunday=False):
        self.day += 28
    
        # February leap year check
        if self.month == 1:
            century = self.year%100 == 0
            if century and self.year%400 == 0:
                left_over = 0
            elif not century and self.year%4 == 0:
                left_over = 0
            else:
                left_over = -1
        else:
            left_over = self.month_days.get(self.month) - self.day

        self.week_day = (self.week_day+left_over+1)%7
        self.month = (self.month + 1)%12
        self.day = 1
        
        if self.month == 0: self.year += 1
        if self.week_day == 0 and self.year != 2001 and count_sunday: self.sunday_counter += 1

sc = SundayCounter()
while sc.year < 1901:
    sc.traverse_months()
while sc.year < 2001:
    sc.traverse_months(True)
print sc.sunday_counter
