import unittest

from assertpy import assert_that

from problems.p072.p072_solution import PrimeDenominatorHandler, CompositeDenominatorHandler, DenominatorHandlerFactory


class PrimeDenominatorHandlerTest(unittest.TestCase):
    def test_calculate_returns_one_less_than_denominator(self):
        assert_that(PrimeDenominatorHandler(17).calculate_number_reduced_numerators()).is_equal_to(16)


class CompositeDenominatorHandlerTest(unittest.TestCase):
    def test_calculate_handles_composite_of_single_prime_with_multiplicity_greater_than_one(self):
        assert_that(CompositeDenominatorHandler(8).calculate_number_reduced_numerators()).is_equal_to(4)

    def test_calculate_handles_composite_of_multiple_primes_with_multiplicity_of_one(self):
        assert_that(CompositeDenominatorHandler(14).calculate_number_reduced_numerators()).is_equal_to(6)

    def test_calculate_handles_composite_of_multiple_primes_with_multiplicity_greater_than_one(self):
        assert_that(CompositeDenominatorHandler(12).calculate_number_reduced_numerators()).is_equal_to(4)


class DenominatorHandlerFactoryTest(unittest.TestCase):
    def test_get_returns_instance_of_PrimeDenominatorHandler_if_denominator_is_prime(self):
        assert_that(DenominatorHandlerFactory().get(23)).is_instance_of(PrimeDenominatorHandler)

    def test_get_returns_instance_of_CompositeDenominatorHandler_if_denominator_is_composite(self):
        assert_that(DenominatorHandlerFactory().get(24)).is_instance_of(CompositeDenominatorHandler)
