"""
https://projecteuler.net/problem=52

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x contain the same digits.
"""

for number in range(1, 1000000):
    list_num = []
    for j in range(0, len(str(number))):
        list_num.append(str(number)[j])
    list_num.sort()

    valid_int = True

    for multiplier in range(2, 7):
        multNum = number * multiplier
        list_multNum = []
        for k in range(0, len(str(multNum))):
            list_multNum.append(str(multNum)[k])
        list_multNum.sort()

        if list_num != list_multNum:
            valid_int = False
            break

    if valid_int:
        print(number)
        break

# 142857
