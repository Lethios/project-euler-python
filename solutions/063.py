"""
https://projecteuler.net/problem=63

The 5-digit number, 16807 = 7⁵, is also a fifth power. Similarly, the 9-digit number, 134217728 = 8⁹, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

count = 0

for power in range(1, 5000):
    for base in range(1, 10):
        if len(str(base ** power)) == 4299:
            print(count)
            exit(0)
        if len(str(base ** power)) == power:
            count += 1

print(count)
# 49
