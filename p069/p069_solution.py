from util.prime import sieve_of_eratosthenes, get_factorization
from util.solutiontimer import time_function

UPPER_BOUND = 10 ** 6


def calculate_totient(n, sieve):
    prime_factorization = get_factorization(n, sieve)

    totient = n
    for prime in prime_factorization:
        totient *= 1 - float(1) / prime
    return totient


def main():
    sieve = sieve_of_eratosthenes(UPPER_BOUND)
    sieve_set = set(sieve)

    n = 2
    highest_totient_division_result = 2

    for i in range(1, UPPER_BOUND):
        if i in sieve_set:
            continue

        totient = calculate_totient(i, sieve)
        division_result = i / totient
        if division_result > highest_totient_division_result:
            highest_totient_division_result = division_result
            n = i

    print 'Maximum totient below {} is {} with totient value of {}.'.format(UPPER_BOUND, n,
                                                                            highest_totient_division_result)


if __name__ == '__main__':
    time_function(main)
