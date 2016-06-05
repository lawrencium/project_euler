from util.prime import sieve_of_eratosthenes
from util.solutiontimer import time_function

__author__ = 'lawrencechen'

PRIME_UPPER_BOUND = 9999999
MAX_PRIME_LENGTH = len(str(PRIME_UPPER_BOUND))
FAMILY_SIZE = 4


def concatenate(n1, n2):
    return int('{}{}'.format(n1, n2))


def concatenation_is_prime(n1, n2, s):
    concatenation = concatenate(n1, n2)
    return concatenation in s


def both_permutations_in_set(n1, n2, s):
    return concatenation_is_prime(n1, n2, s) and concatenation_is_prime(n2, n1, s)


def number_digits(number):
    return len(str(number))


def form_adjacency_list(primes, primes_mod_one, primes_mod_two):
    adjacency_list = {i: {i} for i in primes}

    for source_prime in primes:
        source_price_number_digits = number_digits(source_prime)
        prime_set = primes_mod_one if source_prime % 3 == 1 else primes_mod_two
        for destination_prime in prime_set:
            if number_digits(destination_prime) + source_price_number_digits > MAX_PRIME_LENGTH:
                break

            if destination_prime < source_prime:
                continue
            if both_permutations_in_set(source_prime, destination_prime, primes):
                adjacency_list[source_prime].add(destination_prime)
                adjacency_list[destination_prime].add(source_prime)

    return adjacency_list


def find_largest_family(adjacency_list):
    def calculate_family(family_candidates):
        family = set(family_candidates)
        for candidate in family_candidates:
            family &= adjacency_list[candidate]
        return family

    largest_family = []

    for prime in adjacency_list:
        family = calculate_family(adjacency_list[prime])

        if len(family) > len(largest_family):
            largest_family = family

        if len(largest_family) == FAMILY_SIZE:
            return largest_family

    return largest_family


def solution():
    prime_list = sieve_of_eratosthenes(PRIME_UPPER_BOUND)
    del [prime_list[0]]
    primes_mod_one = [3] + filter(lambda x: x % 3 == 1, prime_list)
    primes_mod_two = [3] + filter(lambda x: x % 3 == 2 and x != 2, prime_list)

    primes = set(prime_list)

    adjacency_list = form_adjacency_list(primes, primes_mod_one, primes_mod_two)

    largest_family = find_largest_family(adjacency_list)

    if len(largest_family) == FAMILY_SIZE:
        print 'Found prime family of size {} :: {}'.format(FAMILY_SIZE, largest_family)
    else:
        print 'Could not find prime family -- generate larger primes :('
        print 'Largest prime family found was of size {} :: {}'.format(len(largest_family), largest_family)


if __name__ == '__main__':
    time_function(solution)
