import unittest

from assertpy import assert_that

from problems.util.prime import get_factorization, sieve_of_eratosthenes


class PrimeFactorizationTest(unittest.TestCase):
    def setUp(self):
        self.sieve = sieve_of_eratosthenes(30)

    def test_returns_prime_factorization_on_prime_number_returns_prime_number_as_only_key(self):
        assert_that(get_factorization(3, self.sieve)).is_equal_to({3: 1})

    def test_returns_prime_factorization_on_composite_number_of_primes_with_multiplicity_one(
            self):
        assert_that(get_factorization(6, self.sieve)).is_equal_to({3: 1, 2: 1})

    def test_handles_composite_numbers_composed_of_primes_with_higher_multiplicities(self):
        assert_that(get_factorization(12, self.sieve)).is_equal_to({3: 1, 2: 2})

    def test_setting_square_root_as_upper_bound_handles_prime_greater_than_upper_bound(self):
        assert_that(get_factorization(14, self.sieve)).is_equal_to({2: 1, 7: 1})

    def test_setting_square_root_as_upper_bound_handles_prime_of_higher_multiplicity_greater_than_upper_bound(self):
        assert_that(get_factorization(2 * 7 ** 3, self.sieve)).is_equal_to({2: 1, 7: 3})

    def test_error_if_sieve_too_small(self):
        with self.assertRaises(RuntimeError):
            get_factorization(31 ** 2, self.sieve)
