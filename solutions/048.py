"""
The series, 1¹ + 2² + 3³ + ··· + 10¹⁰ = 10405071317.

Find the last ten digits of the series, 1¹ + 2² + 3³ + ··· + 1000¹⁰⁰⁰.
"""

def power_sum_series(n):
    number_sum = 0

    for number in range(1, n + 1):
        number_sum += pow(number, number)

    return number_sum

print(str(power_sum_series(1000))[-10:])
# 9110846700
