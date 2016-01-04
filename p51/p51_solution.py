from p51.primetrie import PrimeDigitTrie
from util.prime import sieve_of_eratosthenes
from util.solutiontimer import time_function

__author__ = 'lawrencechen'

NUMBER_DIGITS = 7
FAMILY_SIZE = 8


def number_contains_duplicates(n):
    number_string = str(n)
    return any(number_string.count(digit) > 1 for digit in number_string)


def solution():
    primes = sieve_of_eratosthenes(10 ** NUMBER_DIGITS)

    modified_primes = filter(lambda x: number_contains_duplicates(x) and x > 10 ** (NUMBER_DIGITS - 1),
                                          primes)

    prime_trie = PrimeDigitTrie(NUMBER_DIGITS)
    for prime in modified_primes:
        family = prime_trie.insert(prime)
        if family.count >= FAMILY_SIZE:
            print 'Found %i member family! The smallest prime in this family is %i.' % (
                FAMILY_SIZE, family.smallest_value)
            return

    print 'Could not find a %i prime value family with %i digit prime numbers.' % (FAMILY_SIZE, NUMBER_DIGITS)


if __name__ == '__main__':
    time_function(solution)
