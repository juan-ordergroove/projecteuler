base_dict = {
      1: 'one'
    , 2: 'two'
    , 3: 'three'
    , 4: 'four'
    , 5: 'five'
    , 6: 'six'
    , 7: 'seven'
    , 8: 'eight'
    , 9: 'nine'
    , 10: 'ten'
    , 11: 'eleven'
    , 12: 'twelve'
    , 13: 'thirteen'
    , 14: 'fourteen'
    , 15: 'fifteen'
    , 16: 'sixteen'
    , 17: 'seventeen'
    , 18: 'eighteen'
    , 19: 'nineteen'
    , 20: 'twenty'
    , 30: 'thirty'
    , 40: 'forty'
    , 50: 'fifty'
    , 60: 'sixty'
    , 70: 'seventy'
    , 80: 'eighty'
    , 90: 'ninety'
    }

def get_tens(i):
    char_sum = 0
    tens = (i / 10) * 10
    char_sum += len(base_dict.get(tens))

    ones = i - tens
    if ones > 0: char_sum += len(base_dict.get(ones))
    return char_sum

def get_hundreds(i):
    char_sum = 0
    hundreds = (i / 100)
    char_sum += len(base_dict.get(hundreds))
    char_sum += len('hundred')

    new_i = i - hundreds*100
    if new_i > 0:
        char_sum += len('and')
        if base_dict.get(new_i): char_sum += len(base_dict.get(new_i))
        else: char_sum += get_tens(new_i)
    return char_sum

n = 1000
char_sum = 0
for i in range(1, n+1):
    int_len = len(str(i))
    if base_dict.get(i): char_sum += len(base_dict.get(i))
    elif int_len == 2: char_sum += get_tens(i)
    elif int_len == 3: char_sum += get_hundreds(i)
    elif int_len == 4: char_sum += len('onethousand')
print char_sum
