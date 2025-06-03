"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d₁ be the 1st digit, d₂ be the 2nd digit, and so on. In this way, we note the following:

d₂d₃d₄ = 406 is divisible by 2
d₃d₄d₅ = 063 is divisible by 3
d₄d₅d₆ = 635 is divisible by 5
d₅d₆d₇ = 357 is divisible by 7
d₆d₇d₈ = 572 is divisible by 11
d₇d₈d₉ = 728 is divisible by 13
d₈d₉d₁₀ = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from itertools import permutations

pandigital_list = list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
pandigital_property_list = []

for pandigital_number in pandigital_list:
    pandigital_num = ""
    for number in pandigital_number:
        pandigital_num += str(number)

    is_valid = True
    test_list = [1, 2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        if int(pandigital_num[i] + pandigital_num[i + 1] + pandigital_num[i + 2]) % test_list[i] == 0:
            continue
        else:
            is_valid = False
            break
    
    if is_valid:
        pandigital_property_list.append(int(pandigital_num))

sum = 0
for num in pandigital_property_list:
    sum += num

print(sum)
# 16695334890
