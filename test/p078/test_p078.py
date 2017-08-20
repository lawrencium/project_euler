import unittest

from assertpy import assert_that

from problems.p078.p078_solution import number_piles

__author__ = 'lawrencechen'


class RecursivePileCalculatorTest(unittest.TestCase):
    def test_returns_value_of_one_for_one_coin(self):
        assert_that(number_piles(1)).is_equal_to(1)

    def test_returns_value_of_zero_for_zero_coins(self):
        assert_that(number_piles(0)).is_equal_to(0)

    def test_one_step_above_base_case(self):
        assert_that(number_piles(2)).is_equal_to(2)

    def test_two_steps_above_base_case(self):
        assert_that(number_piles(3)).is_equal_to(3)
