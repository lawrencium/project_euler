import unittest

from assertpy import assert_that

from p078.solution import recursive_calculator

__author__ = 'lawrencechen'


class RecursivePileCalculatorTest(unittest.TestCase):
    def test_returns_value_of_one_for_one_coin(self):
        assert_that(recursive_calculator(1)).is_equal_to(1)

    def test_returns_value_of_zero_for_zero_coins(self):
        assert_that(recursive_calculator(0)).is_equal_to(0)
