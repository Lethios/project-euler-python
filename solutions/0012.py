"""
https://projecteuler.net/problem=12

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, . . .

Let us list the factors of the first seven triangle numbers:

1: 1
3: 1, 3
6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

from math import isqrt

def triangle_number(term):
    return term * (term + 1) // 2

def divisor_check(number):
    divisors = 0

    for i in range(1, isqrt(number) + 1):
        if number % i == 0:
            if i != number:
                divisors += 2
            else:
                divisors = 1

    return divisors

REQUIRED_DIVISORS = 500

DIVISOR = 1
X = 0

while DIVISOR < REQUIRED_DIVISORS:
    X += 1
    NUM = triangle_number(X)
    DIVISOR = divisor_check(NUM)

print(NUM)
# 76576500
