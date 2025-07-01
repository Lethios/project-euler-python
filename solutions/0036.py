"""
https://projecteuler.net/problem=36

The decimal number, 585 = 1001001001₂ (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def is_palindrome(n):
    return str(n) == str(n)[::-1]

PALINDROME_LIST_SUM = 0

for number in range(1, 1000000):
    if is_palindrome(number):
        binary = bin(number)[2:]

        if is_palindrome(binary):
            PALINDROME_LIST_SUM += number

print(PALINDROME_LIST_SUM)
# 872187
