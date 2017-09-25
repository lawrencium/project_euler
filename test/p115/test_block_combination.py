import unittest

from assertpy import assert_that

from problems.p114.block_combination import BlockCombinationCounter


class BlockCombinationCounterTest(unittest.TestCase):
    def test_project_euler_examples(self):
        assert_that(BlockCombinationCounter(3, 29).count()).is_equal_to(673135)
        assert_that(BlockCombinationCounter(3, 30).count()).is_equal_to(1089155)

        assert_that(BlockCombinationCounter(10, 56).count()).is_equal_to(880711)
        assert_that(BlockCombinationCounter(10, 57).count()).is_equal_to(1148904)
