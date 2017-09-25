import unittest

from assertpy import assert_that

from problems.p114.block_combination import BlockCombinationCounter


class SimpleBlockCombinationCountTest(unittest.TestCase):
    def test_minimum_length_and_row_length_same(self):
        counter = BlockCombinationCounter(3, 3)
        assert_that(counter.count()).is_equal_to(2)

    def test_one_iteration_of_recurrence_relation(self):
        counter = BlockCombinationCounter(3, 4)
        assert_that(counter.count()).is_equal_to(4)

    def test_has_correct_total_for_row_of_five_tiles_and_minimum_length_three(self):
        counter = BlockCombinationCounter(3, 7)
        assert_that(counter.count()).is_equal_to(17)
