from util.prime import sieve_of_eratosthenes, is_prime
from util.solutiontimer import time_function

__author__ = 'lawrencechen'

PRIME_UPPER_BOUND = 9999999
FAMILY_SIZE = 4


def concatenate(n1, n2):
    return int('{}{}'.format(n1, n2))


def concatenation_is_prime(n1, n2, s):
    concatenation = concatenate(n1, n2)
    return concatenation in s or is_prime(concatenation)


def both_permutations_in_set(n1, n2, s):
    return concatenation_is_prime(n1, n2, s) and concatenation_is_prime(n2, n1, s)


def form_adjacency_list(primes, primes_mod_one, primes_mod_two):
    adjacency_list = {}
    for source_prime in primes:
        adjacency_list[source_prime] = set()

        prime_set = primes_mod_one if source_prime % 3 == 1 else primes_mod_two
        prime_set = filter(lambda x: x > source_prime, prime_set)

        print source_prime, len(prime_set)
        for destination_prime in prime_set:
            if both_permutations_in_set(source_prime, destination_prime, primes):
                adjacency_list[source_prime].add(destination_prime)

    return adjacency_list


def solution():
    prime_list = sieve_of_eratosthenes(PRIME_UPPER_BOUND)
    del [prime_list[0]]
    primes_mod_one_list = [3] + filter(lambda x: x % 3 == 1, prime_list)
    primes_mod_two_list = [3] + filter(lambda x: x % 3 == 2 and x != 2, prime_list)

    primes = set(prime_list)
    primes_mod_one = set(primes_mod_one_list)
    primes_mod_two = set(primes_mod_two_list)

    adjacency_list = form_adjacency_list(primes, primes_mod_one, primes_mod_two)

    print 'Could not find prime family -- generate larger primes :('


if __name__ == '__main__':
    time_function(solution)
