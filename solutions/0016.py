"""
https://projecteuler.net/problem=16

2¹⁵ = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2¹⁰⁰⁰?
"""

def power_digit_sum(base, power):
    power_num = str(int(pow(base, power)))
    power_sum = 0

    for index in range(0, len(power_num)):
        power_sum += int(power_num[index])

    return print(power_sum)

power_digit_sum(2, 1000)
# 1366
