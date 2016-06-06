from util.prime import sieve_of_eratosthenes
from util.solutiontimer import time_function

__author__ = 'lawrencechen'

PRIME_UPPER_BOUND = 99999999
MAX_PRIME_LENGTH = len(str(PRIME_UPPER_BOUND))
FAMILY_SIZE = 5


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
        source_prime_number_digits = number_digits(source_prime)
        prime_set = prime_set_factory(source_prime, primes_mod_one, primes_mod_two, primes)

        for destination_prime in prime_set:
            if number_digits(destination_prime) + source_prime_number_digits > MAX_PRIME_LENGTH:
                if source_prime == 3:
                    continue
                else:
                    break
            if destination_prime <= source_prime:
                continue
            if both_permutations_in_set(source_prime, destination_prime, primes):
                adjacency_list[source_prime].add(destination_prime)
                adjacency_list[destination_prime].add(source_prime)

    return adjacency_list


def prime_set_factory(source_prime, primes_mod_one, primes_mod_two, primes):
    if source_prime % 3 == 1:
        return primes_mod_one
    elif source_prime % 3 == 2:
        return primes_mod_two
    else:
        return primes


def find_largest_family(adjacency_list):
    found_family = False
    sources = adjacency_list.keys()

    for p1 in sources:
        candidates1 = adjacency_list[p1]
        if len(candidates1) < FAMILY_SIZE:
            continue
        for p2 in candidates1:
            if p2 <= p1:
                continue
            candidates2 = adjacency_list[p2]
            if len(candidates2) < FAMILY_SIZE:
                continue
            for p3 in candidates2:
                if p3 <= p2:
                    continue
                if p3 not in candidates1:
                    continue
                candidates3 = adjacency_list[p3]
                if len(candidates3) < FAMILY_SIZE:
                    continue
                for p4 in candidates3:
                    if p4 <= p3:
                        continue
                    if p4 not in candidates1 or p4 not in candidates2:
                        continue
                    candidates4 = adjacency_list[p4]
                    if len(candidates4) < FAMILY_SIZE:
                        continue
                    for p5 in candidates4:
                        if p5 <= p4:
                            continue
                        if p5 not in candidates1 or p5 not in candidates2 or p5 not in candidates3:
                            continue
                        print 'Found a family of size 5 :: {} {} {} {} {}'.format(p1, p2, p3, p4, p5)
                        found_family = True
    return found_family


def solution():
    print 'Generating primes up to {}...'.format(PRIME_UPPER_BOUND)
    prime_list = sieve_of_eratosthenes(PRIME_UPPER_BOUND)
    del [prime_list[0]]
    primes_mod_one = [3] + filter(lambda x: x % 3 == 1, prime_list)
    primes_mod_two = [3] + filter(lambda x: x % 3 == 2 and x != 2, prime_list)

    primes = set(prime_list)

    print 'Finished generating primes'

    adjacency_list = form_adjacency_list(primes, primes_mod_one, primes_mod_two)

    print 'Finished creating adjacency list'

    if not find_largest_family(adjacency_list):
        print 'Could not find prime family -- generate larger primes :('


if __name__ == '__main__':
    time_function(solution)
