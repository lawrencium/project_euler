import math

__author__ = 'lawrencechen'


def sieve_of_eratosthenes(n):
    """
    returns all primes less than or equal to n
    :param n: upper bound for sieve
    """
    if n < 2:
        return []
    sieve = [True for _ in xrange((n - 1) / 2 + 1)]  # gets

    for sieve_ind in xrange(1, len(sieve)):
        if sieve_ind:
            val_at_ind = 2 * sieve_ind + 1
            if val_at_ind ** 2 > n:
                break
            for composite in xrange(val_at_ind + 2 * val_at_ind, n + 1, 2 * val_at_ind):
                composite_ind = (composite - 1) / 2
                sieve[composite_ind] = False
    return [2] + [2 * i + 1 for i in xrange(1, len(sieve)) if sieve[i]]


def get_factorization(n, factors):
    """
    returns factorization of n in key value pairs (k,v) where is the factor and v is its multiplicity

    For example, prime_factorization(12, prime_numbers_up_to_5) = {2:2, 3:1}
    :param n: number to take prime factorization of
    :param factors: a list of factors to decompose n into -- it is required that the list of factors be sorted
    :return: dictionary representing prime factorization
    """

    def get_multiplicity(number, factor):
        count = 0
        while number % factor == 0:
            number /= factor
            count += 1
        return count

    last_prime = filter(lambda x: x <= n, factors)[-1]

    if n == last_prime:
        return {n: 1}

    factorization = {}
    upper_bound = n / 2
    for prime in factors:
        if prime > upper_bound:
            break
        if n % prime == 0:
            multiplicity = get_multiplicity(n, prime)
            factorization[prime] = multiplicity

    return factorization


def is_prime(n):
    """
    naively checks to see if number is prime
    :param n: number to check
    :return: True if n is prime False otherwise
    """
    if n % 2 == 0:
        return False
    for i in xrange(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
