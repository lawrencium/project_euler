from util.prime import get_factorization, sieve_of_eratosthenes

__author__ = 'lawrencechen'

import unittest
from assertpy import assert_that


class PrimeFactorizationTest(unittest.TestCase):
    def setUp(self):
        self.sieve = sieve_of_eratosthenes(10)

    def test_returns_prime_factorization_on_prime_number_returns_prime_number_as_only_key(self):
        assert_that(get_factorization(3, self.sieve)).is_equal_to({3: 1})

    def test_returns_prime_factorization_on_composite_number_of_primes_with_multiplicity_one(
            self):
        assert_that(get_factorization(6, self.sieve)).is_equal_to({3: 1, 2: 1})

    def test_factorization_handles_composite_numbers_composed_of_primes_with_higher_multiplicities(self):
        assert_that(get_factorization(12, self.sieve)).is_equal_to({3: 1, 2: 2})
