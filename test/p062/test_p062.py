import unittest

from assertpy import assert_that

from problems.p062.p062_solution import PermutationTracker


class PermutationTrackerTest(unittest.TestCase):
    def test_single_insert_returns_falsy_if_termination_condition_not_met(self):
        tracker = PermutationTracker(999)
        assert_that(tracker.insert(123)).is_none()

    def test_single_insert_returns_truthy_if_termination_condition_met(self):
        tracker = PermutationTracker(1)
        assert_that(tracker.insert(123)).is_true()

    def test_multiple_inserts_of_same_number_returns_falsy_until_termination_condition_is_met(self):
        stopping_condition = 10
        tracker = PermutationTracker(stopping_condition)
        [assert_that(tracker.insert(123)).is_false() for _ in range(stopping_condition - 1)]
        assert_that(tracker.insert(123)).is_true()

    def test_handles_permutations(self):
        tracker = PermutationTracker(2)
        tracker.insert(123)
        assert_that(tracker.insert(321)).is_true()

    def test_returns_first_permutation_upon_stopping_condition(self):
        tracker = PermutationTracker(3)
        tracker.insert(123)
        tracker.insert(312)
        assert_that(tracker.insert(231)).is_equal_to(123)
