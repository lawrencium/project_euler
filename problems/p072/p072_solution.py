from abc import abstractmethod

from problems.util.prime import sieve_of_eratosthenes, get_factorization
from problems.util.solutiontimer import time_function

d = 1000000
# d = 8
sieve = sieve_of_eratosthenes(d)
sieve_set = set(sieve)


def main():
    number_reduced_fractions = 0
    factory = DenominatorHandlerFactory()
    for denominator in range(2, d + 1):
        number_reduced_fractions += factory.get(denominator).calculate_number_reduced_numerators()

    print number_reduced_fractions


class DenominatorHandler(object):
    def __init__(self, denominator):
        self._denominator = denominator

    @abstractmethod
    def calculate_number_reduced_numerators(self):
        pass


class PrimeDenominatorHandler(DenominatorHandler):
    def calculate_number_reduced_numerators(self):
        return self._denominator - 1


class CompositeDenominatorHandler(DenominatorHandler):
    def calculate_number_reduced_numerators(self):
        return calculate_totient(self._denominator)


class DenominatorHandlerFactory(object):
    def get(self, denominator):
        return PrimeDenominatorHandler(denominator) if denominator in sieve_set else CompositeDenominatorHandler(
            denominator)


def calculate_totient(n):
    prime_factorization = get_factorization(n, sieve)

    totient = n
    for prime in prime_factorization:
        totient *= 1 - float(1) / prime
    return int(totient)


if __name__ == '__main__':
    time_function(main)
