import math
import sys

def prime_factors(natural_number):
    return get_factors(natural_number)

def get_factors(number, prime=2, factors=[]):
    if number <= 1:
        return factors
    while number % prime:
        prime += 1 
    return get_factors(number / prime, prime, factors + [prime])
