"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
def eratosthenes_sieve(limit):
    prime_list = [True] * (limit + 1)
    prime_list[0], prime_list[1] = False, False

    prime_sum = 0

    for num, prime in enumerate(prime_list):
        if prime:
            prime_sum += num
            for i in range(num * 2, limit + 1, num):
                prime_list[i] = False

    return prime_sum

print(eratosthenes_sieve(2000000))
# 142913828922
