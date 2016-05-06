from util.prime import sieve_of_eratosthenes
from util.solutiontimer import time_function

__author__ = 'lawrencechen'

HIGHEST_PRIME = 9999999


def concatenate(n1, n2):
    return int('{}{}'.format(n1, n2))


def solution():
    primes = sieve_of_eratosthenes(HIGHEST_PRIME)
    prime_set = set(primes)

    num_primes = len(primes)
    for i1 in xrange(num_primes):
        prime1 = primes[i1]
        for i2 in xrange(i1, num_primes):
            prime2 = primes[i2]
            for i3 in xrange(i2, num_primes):
                prime3 = primes[i3]
                for i4 in xrange(i3, num_primes):
                    prime4 = primes[i4]


if __name__ == '__main__':
    time_function(solution)
