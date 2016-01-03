import unittest

from assertpy import assert_that

from p121.disk_game import DiskGame

__author__ = 'lawrencechen'

ONE_AS_FLOAT = float(1)
ERROR_MARGIN = 0.01


class OneRoundDiskGameTest(unittest.TestCase):
    def test_correct_probability_for_game_with_one_rounds(self):
        assert_that(DiskGame.win_probability(1, 1, 0)).is_equal_to(ONE_AS_FLOAT / 2)


class TwoRoundDiskGameTest(unittest.TestCase):
    def test_correct_probability_for_two_round_game_currently_at_second_round_with_one_observed_blue_disk(self):
        expected = ONE_AS_FLOAT / 3
        assert_that(DiskGame.win_probability(2, 2, 1)).is_equal_to(expected)

    def test_correct_probability_for_two_round_game_currently_at_second_round_with_zero_observed_blue_disks(self):
        assert_that(DiskGame.win_probability(2, 2, 0)).is_equal_to(0)

    def test_correct_probability_for_two_round_game(self):
        expected = ONE_AS_FLOAT / 6
        assert_that(DiskGame.win_probability(2, 1, 0)).is_equal_to(expected)


class ThreeRoundDiskGameTest(unittest.TestCase):
    def test_correct_probability_for_three_round_game_currently_at_second_round_with_zero_observed_blue_disks(self):
        assert_that(DiskGame.win_probability(3, 2, 0)).is_equal_to(ONE_AS_FLOAT / 12)

    def test_correct_probability_for_three_round_game_currently_at_second_round_with_one_observed_blue_disk(self):
        assert_that(DiskGame.win_probability(3, 2, 1)).is_equal_to(0.5)

    def test_correct_probability_for_three_round_game(self):
        expected = 0.29
        assert_that(DiskGame.win_probability(3, 1, 0)).is_close_to(expected, ERROR_MARGIN)


class FourRoundDiskGame(unittest.TestCase):
    def test_correct_probability_for_four_round_game(self):
        expected = ONE_AS_FLOAT * 11 / 120
        assert_that(DiskGame.win_probability(4, 1, 0)).is_close_to(expected, ERROR_MARGIN)
