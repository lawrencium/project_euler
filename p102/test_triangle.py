import unittest

from assertpy import assert_that

from p102.triangle import Triangle, LineSegmentIntercept

__author__ = 'lawrencechen'


class TriangleOverlapOriginTest(unittest.TestCase):
    def test_no_overlap_if_points_all_have_negative_x_values(self):
        triangle = Triangle((-1, 0), (-10, 1), (-11, 3))
        assert_that(triangle.overlap_origin()).is_false()

    def test_no_overlap_if_points_all_have_positive_x_values(self):
        triangle = Triangle((1, 0), (10, 1), (11, 3))
        assert_that(triangle.overlap_origin()).is_false()

    def test_no_overlap_if_points_all_have_negative_y_values(self):
        triangle = Triangle((1, -10), (-10, -1), (11, -3))
        assert_that(triangle.overlap_origin()).is_false()

    def test_no_overlap_if_points_all_have_positive_y_values(self):
        triangle = Triangle((1, 10), (-10, 1), (11, 3))
        assert_that(triangle.overlap_origin()).is_false()

    def test_no_overlap_if_y_intercepts_of_triangle_have_the_same_sign(self):
        triangle = Triangle((2, 2), (1, 0), (-1, 2))
        assert_that(triangle.overlap_origin()).is_false()

    def test_no_overlap_if_points_are_in_same_quadrant(self):
        triangle = Triangle((1, 1), (2, 2), (3, 3))
        assert_that(triangle.overlap_origin()).is_false()

    def test_overlap_exists_if_a_vertex_is_on_origin(self):
        triangle = Triangle((-1, -1), (1, -1), (0, 0))
        assert_that(triangle.overlap_origin()).is_true()

    def test_overlap_in_case_where_each_point_is_in_different_quadrant(self):
        triangle = Triangle((2, 2), (2, -2), (-2, 1))
        assert_that(triangle.overlap_origin()).is_true()

    def test_no_overlap_in_case_where_points_are_in_two_adjacent_quadrants(self):
        triangle = Triangle((2, 2), (1, 3), (-2, 1))
        assert_that(triangle.overlap_origin()).is_false()

    def test_overlap_in_case_where_points_are_in_opposite_quadrants(self):
        triangle = Triangle((2, 2), (1, 3), (-2, -3))
        assert_that(triangle.overlap_origin()).is_true()

    def test_non_overlapping_large_triangle(self):
        triangle = Triangle((558, -118), (465, 461), (-568, -909))
        assert_that(triangle.overlap_origin()).is_false()

    def test_first_euler_example(self):
        triangle = Triangle((-340, 495), (-153, -910), (835, -947))
        assert_that(triangle.overlap_origin()).is_true()

    def test_overlap_exists_if_triangle_intersects_positive_and_negative_axes_for_both_x_and_y_axis(self):
        triangle = Triangle((-1, -1), (1, -1), (0, 1))
        assert_that(triangle.overlap_origin()).is_true()


class YInterceptTest(unittest.TestCase):
    def setUp(self):
        self.intercept = LineSegmentIntercept

    def test_returns_negative_one_in_x_value_if_two_points_do_not_intercept_y_axis(self):
        assert_that(self.intercept.y_intercept((3, 3), (2, 2))[0]).is_equal_to(-1)

    def test_returns_zero_in_x_value_if_line_segment_intercepts_y_axis(self):
        assert_that(self.intercept.y_intercept((3, 3), (-1, 2))[0]).is_equal_to(0)

    def test_returns_intercept_as_y_value_if_line_segment_intercepts_y_axis(self):
        assert_that(self.intercept.y_intercept((3, 3), (-2, 4))[1]).is_equal_to(3.6)

    def test_no_funky_business_on_horizontal_line(self):
        assert_that(self.intercept.y_intercept((-1, 1), (1, 1))).is_equal_to((0, 1))

    def test_returns_negative_one_in_x_value_if_line_segment_is_vertical_line(self):
        assert_that(self.intercept.y_intercept((0, 1), (0, 2))[0]).is_equal_to(-1)
