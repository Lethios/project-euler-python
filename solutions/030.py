"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴

8208 = 8⁴ + 2⁴ + 0⁴ + 8⁴

9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴

As 1 = 1⁴ is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

fifth_power_numbers = []
FIFTH_POWER_NUMBERS_SUM = 0

for i in range(2, 1000000):
    FIFTH_POWER = 0

    for index in range(0, len(str(i))):
        FIFTH_POWER += pow(int(str(i)[index]), 5)

    if FIFTH_POWER == i:
        fifth_power_numbers.append(i)

for number in fifth_power_numbers:
    FIFTH_POWER_NUMBERS_SUM += number

print(FIFTH_POWER_NUMBERS_SUM)
# 443839
