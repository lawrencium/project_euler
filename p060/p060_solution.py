from util.prime import sieve_of_eratosthenes
from util.solutiontimer import time_function

__author__ = 'lawrencechen'

HIGHEST_PRIME = 9999999


def concatenate(n1, n2):
    return int('{}{}'.format(n1, n2))


def concatenation_in_set(n1, n2, s):
    return concatenate(n1, n2) in s


def both_permutations_in_set(n1, n2, s):
    return concatenation_in_set(n1, n2, s) and concatenation_in_set(n2, n1, s)


def check_primes(primes_to_use, prime_set_to_use):
    length = len(primes_to_use)
    for i1 in xrange(length):
        prime1 = primes_to_use[i1]
        for i2 in xrange(i1 + 1, length):
            prime2 = primes_to_use[i2]
            if not both_permutations_in_set(prime1, prime2, prime_set_to_use):
                continue
            for i3 in xrange(i2 + 1, length):
                prime3 = primes_to_use[i3]
                if not both_permutations_in_set(prime1, prime3, prime_set_to_use):
                    continue
                if not both_permutations_in_set(prime2, prime3, prime_set_to_use):
                    continue
                for i4 in xrange(i3 + 1, length):
                    prime4 = primes_to_use[i4]
                    if not both_permutations_in_set(prime1, prime4, prime_set_to_use):
                        continue
                    if not both_permutations_in_set(prime2, prime4, prime_set_to_use):
                        continue
                    if not both_permutations_in_set(prime3, prime4, prime_set_to_use):
                        continue
                    for i5 in xrange(i4 + 1, length):
                        prime5 = primes_to_use[i5]
                        if not both_permutations_in_set(prime1, prime5, prime_set_to_use):
                            continue
                        if not both_permutations_in_set(prime2, prime5, prime_set_to_use):
                            continue
                        if not both_permutations_in_set(prime3, prime5, prime_set_to_use):
                            continue
                        if not both_permutations_in_set(prime4, prime5, prime_set_to_use):
                            continue
                        print 'Found this prime set :: {}, {}, {}, {}'.format(prime1, prime2, prime3, prime4)
                        return True
    return False


def solution():
    primes = sieve_of_eratosthenes(HIGHEST_PRIME)
    prime_set = set(primes)

    primes_mod_one = [3] + [i for i in primes if i % 3 == 1]
    primes_mod_two = [3] + [i for i in primes if i % 3 == 2]

    if check_primes(primes_mod_one, prime_set):
        return
    if check_primes(primes_mod_two, prime_set):
        return

    print 'Could not find prime family -- generate larger primes :('


if __name__ == '__main__':
    time_function(solution)
