"""
https://projecteuler.net/problem=53

There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, C(5,3) = 10.
In general, C(n,r) = n!/(r!(n-r)!), where r ≤ n, n! = n × (n-1) × ... × 3 × 2 × 1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: C(23,10) = 1144066.

How many, not necessarily distinct, values of C(n,r) for 1 ≤ n ≤ 100, are greater than one-million?
"""
from math import comb

ans_count = 0

for n in range(1, 101):
    for r in range(1, n):
        if comb(n, r) > 1_000_000:
            ans_count += 1

print(ans_count)
# 4075
