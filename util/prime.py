__author__ = 'lawrencechen'


def sieve_of_eratosthenes(n):
    """
    returns all primes less than or equal to n
    """
    if n < 2:
        return []
    sieve = [True for i in xrange((n - 1) / 2 + 1)]  # gets

    for sieve_ind in xrange(1, len(sieve)):
        if sieve_ind:
            val_at_ind = 2 * sieve_ind + 1
            if val_at_ind ** 2 > n: break
            for composite in xrange(val_at_ind + 2 * val_at_ind, n + 1, 2 * val_at_ind):
                composite_ind = (composite - 1) / 2
                sieve[composite_ind] = False
    return [2] + [2 * i + 1 for i in xrange(1, len(sieve)) if sieve[i]]