"""
n! means n x (n-1) x ··· x 3 x 2 x 1.

For example, 10! = 10 x 9 x ··· x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!.
"""

from math import factorial as fac

def factorial_digit_sum(number):
    factorial = fac(number)
    num_sum = 0

    for index in range(0, len(str(factorial))):
        num_sum += int(str(factorial)[index])

    return num_sum

print(factorial_digit_sum(100))
# 648
