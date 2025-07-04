"""
https://projecteuler.net/problem=45

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle
Tₙ = n(n+1)/2 1, 3, 6, 10, 15, ...

Pentagonal
Pₙ = n(3n-1)/2 1, 5, 12, 22, 35, ...

Hexagonal
Hₙ = n(2n-1) 1, 6, 15, 28, 45, ...

It can be verified that T₂₈₅ = P₁₆₅ = H₁₄₃ = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""

def triangle_number(n):
    number_list = []

    for i in range(1, n + 1):
        number = i * (i + 1) // 2
        number_list.append(number)

    return number_list

def pentagonal_number(n):
    number_list = []

    for i in range(1, n + 1):
        number = i * (3 * i - 1) // 2
        number_list.append(number)

    return number_list

def hexagonal_number(n):
    number_list = []

    for i in range(1, n + 1):
        number = i * (2 * i - 1)
        number_list.append(number)

    return number_list

limit = 1000000
triangle_list = triangle_number(limit)
pentagonal_list = pentagonal_number(limit)
hexagonal_list = hexagonal_number(limit)

intersection_set = set(triangle_list) & set(pentagonal_list) & set(hexagonal_list)
print(intersection_set)
# 1533776805
