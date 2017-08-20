import unittest

from assertpy import assert_that

from problems.p145.p145_solution import reverse_number, naive_checker, sum_contains_all_odd_digits, pivot_check, is_even


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
        assert_that(naive_checker(36)).is_true()

    def test_is_reversible_on_non_reversible_number_returns_false(self):
        assert_that(naive_checker(123)).is_false()

    def test_is_even_returns_true_on_even_number(self):
        assert_that(is_even(2)).is_true()


class PivotCheckTest(unittest.TestCase):
    def test_pivot_check_returns_true_if_length_of_number_is_even(self):
        assert_that(pivot_check(12)).is_true()

    def test_pivot_returns_false_if_sum_of_preceding_digits_does_not_have_carry(self):
        assert_that(pivot_check(102)).is_false()

    def test_pivot_returns_false_if_preceding_digit_has_even_digit_in_ones_place(self):
        assert_that(pivot_check(909)).is_false()

    def test_pivot_returns_false_if_carryover_from_mid_point_causes_surrounding_digits_to_have_even_sum(self):
        assert_that(pivot_check(695)).is_false()
