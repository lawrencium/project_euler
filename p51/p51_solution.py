from util.prime import sieve_of_eratosthenes
from util.solutiontimer import time_function

__author__ = 'lawrencechen'

NUMBER_DIGITS = 6
FAMILY_SIZE = 8


class FamilyInformation(object):
    def __init__(self, lowest_value, count):
        self._lowest_value = lowest_value
        self._count = count

    @property
    def count(self):
        return self._count

    @property
    def lowest_value(self):
        return self._lowest_value


class FamilyTracker(FamilyInformation):
    def __init__(self, lowest_value):
        super(FamilyTracker, self).__init__(lowest_value, 0)

    def increment(self):
        self._count += 1

    def to_immutable_object(self):
        return FamilyInformation(self._lowest_value, self._count)


class FamilyTable(object):
    def __init__(self):
        self.__table = {}

    def increment(self, family, original_number):
        information = self.__search(family, original_number)
        information.increment()
        return information.to_immutable_object()

    def __search(self, family, original_number):
        if family in self.__table:
            return self.__table[family]
        else:
            information = FamilyTracker(original_number)
            self.__table[family] = information
            return information


def number_contains_duplicates(n):
    number_string = str(n)
    return any(number_string.count(digit) > 1 for digit in number_string)


def permute_families(n):
    def specific_family_class(value, replaceable_digit):
        if len(value) == 1:
            return {value[0], '*'} if value[0] == replaceable_digit else {value[0]}
        else:
            family_class = specific_family_class(value[1:], replaceable_digit)
            original_class = {value[0] + i for i in family_class}
            if value[0] == replaceable_digit:
                return original_class | {'*' + i for i in family_class}
            else:
                return original_class

    if n < 0:
        raise Exception('Cannot take family of negative input')

    n_string = str(n)
    families = set()
    for digit in set(n_string):
        families |= specific_family_class(n_string, digit)

    return families


def solution():
    primes = sieve_of_eratosthenes(10 ** NUMBER_DIGITS)

    modified_primes = filter(lambda x: number_contains_duplicates(x) and x > 10 ** (NUMBER_DIGITS - 1),
                             primes)

    family_table = FamilyTable()
    for prime in modified_primes:
        families = permute_families(prime)
        for family_class in families:
            information = family_table.increment(family_class, prime)
            if information.count >= FAMILY_SIZE:
                print 'Found %i member family! The smallest prime in this family is %i.' % (
                    FAMILY_SIZE, information.lowest_value)
                return

    print 'Could not find a %i prime value family with %i digit prime numbers.' % (FAMILY_SIZE, NUMBER_DIGITS)


if __name__ == '__main__':
    time_function(solution)
