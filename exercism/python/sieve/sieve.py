import math


def is_prime(*, number: int):
    stop = int(math.sqrt(number)) + 1
    return all(number % divisor != 0 for divisor in range(2, stop))


def filter_and_conquer(*, numbers, primes=[]):
    if len(numbers) == 0:
        return primes
    if is_prime(number=numbers[0]):
        after_filtering_multiples = list(filter(lambda x: x %
                                                numbers[0] != 0, numbers[1:]))
        return filter_and_conquer(numbers=after_filtering_multiples,
                                  primes=primes + [numbers[0]])


def sieve(limit):
    return filter_and_conquer(numbers=[number for number in range(2, limit + 1)])
