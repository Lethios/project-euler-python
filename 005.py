"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

Find the smallest number that is evenly divisible by all of the numbers from 1 to 20.
"""

from math import lcm
from functools import reduce

def smallest_number(limit):
    num_list = [0] * limit

    for i in range(0, limit):
        num_list[i] = i + 1

    LCM = reduce(lcm, num_list)
    return LCM

print(smallest_number(20))
# 232792560
