import math

def sieve(limit):
    limit += 1
    primes = set([x for x in range(2, limit)])
    #deleting all multiples of 2
    cross_off(primes, 2, limit)
    #iterating over odd numbers until sqrt of limit
    for i in range(3, math.ceil(math.sqrt(limit)), 2):
        cross_off(primes, i, limit)

    return list(primes)

def cross_off(primes, n, limit):
    for i in range(n*n, limit, n):
        if i in primes: 
            primes.remove(i)
            
#def is_prime(*, number: int):
#    stop = int(math.sqrt(number)) + 1
#    return all(number % divisor != 0 for divisor in range(2, stop))
#
#
#def filter_and_conquer(*, numbers, primes=[]):
#    if len(numbers) == 0:
#        return primes
#    if is_prime(number=numbers[0]):
#        after_filtering_multiples = list(filter(lambda x: x %
#                                                numbers[0] != 0, numbers[1:]))
#        return filter_and_conquer(numbers=after_filtering_multiples,
#                                  primes=primes + [numbers[0]])
#
#
#def sieve(limit):
#    return filter_and_conquer(numbers=[number for number in range(2, limit + 1)])


