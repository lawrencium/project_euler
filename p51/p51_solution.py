from util.prime import sieve_of_eratosthenes
from util.solutiontimer import time_function

__author__ = 'lawrencechen'

NUMBER_DIGITS = 5


def number_contains_duplicates(n):
    number_string = str(n)
    return any(number_string.count(digit) > 1 for digit in number_string)


def solution():
    primes = sieve_of_eratosthenes(10 ** NUMBER_DIGITS)
    print filter(lambda x: number_contains_duplicates(x) and x > 10 ** (NUMBER_DIGITS - 1), primes)


if __name__ == '__main__':
    time_function(solution)
