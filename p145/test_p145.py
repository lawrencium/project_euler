import unittest

from assertpy import assert_that

from p145.p145_solution import reverse_number, naive_check_reversibility, sum_contains_all_odd_digits


class P145Test(unittest.TestCase):
    def test_reverse_with_nonzero_trailing_and_leading_digits(self):
        assert_that(reverse_number(123)).is_equal_to(321)

    def test_reverse_with_trailing_zero_returns_number_without_leading_zero(self):
        assert_that(reverse_number(1230)).is_equal_to(321)

    def test_returns_true_if_all_digits_in_sum_are_odd(self):
        assert_that(sum_contains_all_odd_digits(11, 22)).is_true()

    def test_returns_false_if_at_least_one_odd_digit_in_sum(self):
        assert_that(sum_contains_all_odd_digits(11, 21)).is_false()

    def test_is_reversible_on_reversible_number_returns_true(self):
        assert_that(naive_check_reversibility(36)).is_true()

    def test_is_reversible_on_non_reversible_number_returns_false(self):
        assert_that(naive_check_reversibility(123)).is_false()
