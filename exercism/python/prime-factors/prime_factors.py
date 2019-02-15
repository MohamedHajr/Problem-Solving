import math


def prime_factors(n):
    factors = []
    # Print the number of two's that divide n
    while n % 2 == 0:
        factors.append(2)
        n = n / 2

    # # n must be odd at this point
    # # so a skip of 2 ( i = i + 2) can be used
    # for i in range(3, int(math.sqrt(n))+1, 2):

    #     # while i divides n , print i ad divide n
    #     while n % i == 0:
    #         factors.append(i),
    #         n = n / i

    # # Condition if n is a prime
    # # number greater than 2
    # if n > 2:
    #     factors.append(n)
    # return factors
    return get_factors(int(math.sqrt(n))+1, 3, factors)


def get_factors(number, factor=3, factors=[]):
    if number == 1:
        return factors
    if number % factor == 0:
        return get_factors(number / factor, factor, factors + [factor])
    else:
        return get_factors(number, factor + 2, factors)
