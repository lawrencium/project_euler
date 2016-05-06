import unittest

from assertpy import assert_that

from p060.p060_solution import concatenate


class ConcatenationTest(unittest.TestCase):
    def test_concatenate_returns_integer_of_two_numbers_concatenated(self):
        assert_that(concatenate(20, 45)).is_equal_to(2045)
