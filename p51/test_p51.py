import unittest

from assertpy import assert_that

from p51.p51_solution import family

__author__ = 'lawrencechen'


class TestFamily(unittest.TestCase):
    def test_family_throws_error_on_negative_input(self):
        with self.assertRaises(Exception):
            family(-1)

    def test_family_of_single_digit_number_yields_two_element_set(self):
        expected = {'*', '1'}
        assert_that(family(1)).is_equal_to(expected)
