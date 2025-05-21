"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1.

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

memo = {1: 0}

LONGEST_CHAIN = 0
LONGEST_CHAIN_NUMBER = 0

def collatz_chain(number):
    if number in memo:
        return memo[number]

    if number % 2 == 0:
        next_number = number // 2        
    else:
        next_number = 3 * number + 1   

    memo[number] = 1 + collatz_chain(next_number)
    return memo[number]

for i in range(2, 1000000):
    chain = collatz_chain(i)

    if chain > LONGEST_CHAIN:
        LONGEST_CHAIN = chain
        LONGEST_CHAIN_NUMBER = i

print(LONGEST_CHAIN_NUMBER)
# 837799
