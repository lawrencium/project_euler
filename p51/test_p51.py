import unittest

from assertpy import assert_that

from p51.p51_solution import permute_families

__author__ = 'lawrencechen'


class TestFamily(unittest.TestCase):
    def test_family_throws_error_on_negative_input(self):
        with self.assertRaises(Exception):
            permute_families(-1)

    def test_single_digit_number_yields_two_element_family(self):
        expected = {'*', '1'}
        assert_that(permute_families(1)).is_equal_to(expected)

    def test_two_digit_number_with_duplicate_digits_yields_four_element_family(self):
        expected = {'*1', '1*', '**', '11'}
        assert_that(permute_families(11)).is_equal_to(expected)

    def test_two_digit_number_with_distinct_digits_yields_three_element_family(self):
        expected = {'*2', '1*', '12'}
        assert_that(permute_families(12)).is_equal_to(expected)

    def test_number_with_consecutive_duplicates(self):
        expected = {'56333', '56***', '56**3', '56*33', '56*3*', '563**', '5633*', '563*3',
                    '*6333', '5*333'
                    }
        assert_that(permute_families(56333)).is_equal_to(expected)
