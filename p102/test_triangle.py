import unittest

from assertpy import assert_that

from triangle import Triangle

__author__ = 'lawrencechen'


class TriangleOverlapOriginTest(unittest.TestCase):
    def test_no_overlap_if_points_are_in_same_quadrant(self):
        triangle = Triangle((1, 1), (2, 2), (3, 3))
        assert_that(triangle.overlap_origin()).is_false()

    def test_overlap_on_triangle_centered_over_origin(self):
        triangle = Triangle((-1, -1), (1, -1), (0, 1))
        assert_that(triangle.overlap_origin()).is_true()
