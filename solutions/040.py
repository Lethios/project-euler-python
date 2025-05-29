"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dₙ represents the nth digit of the fractional part, find the value of the following expression.

d₁ x d₁₀ x d₁₀₀ x d₁₀₀₀ x d₁₀₀₀₀ x d₁₀₀₀₀₀ x d₁₀₀₀₀₀₀
"""

def champernowne_constant(n):
    constant = "0."
    count = 1

    while len(constant) < n + 2:
        constant += str(count)
        count += 1

    return constant

frac = champernowne_constant(1000000)
product = int(frac[2]) * int(frac[11]) * int(frac[101]) * int(frac[1001]) * int(frac[10001]) * int(frac[100001]) * int(frac[1000001])

print(product)
# 210
