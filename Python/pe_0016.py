#!/usr/bin/python3


def find_sum_of_digits(n: int):
    digit_string_list = list(str(n))
    digit_sum = 0
    for i in digit_string_list:
        digit_sum += int(i)
    return digit_sum

  
def find_exponent_sum(base: int, exponent: int):
    power = base**exponent
    power_digit_sum = find_sum_of_digits(power)
    return power_digit_sum

  
two_power_thousand_sum = find_exponent_sum(base=2, exponent=1000)
print(two_power_thousand_sum)
