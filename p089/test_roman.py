import unittest

from assertpy import assert_that

from p089.roman import compress, starting_index_of_n_consecutive_occurrences


class CompressionTest(unittest.TestCase):
    def test_compressor_returns_original_numeral_on_strings_less_than_four_characters(self):
        assert_that(compress('III')).is_equal_to('III')

    def test_compressor_returns_original_numeral_if_all_characters_are_M(self):
        assert_that(compress('MMMM')).is_equal_to('MMMM')

    def test_compressor_returns_original_numeral_if_no_character_appears_four_consecutive_times(self):
        assert_that(compress('MMLIII')).is_equal_to('MMLIII')

    def test_compressor_returns_two_chracter_substitute_on_string_with_four_consecutive_repeats(self):
        assert_that(compress('XXXX')).is_equal_to('XL')

    def test_compressor_returns_original_numeral_if_repeating_character_is_M(self):
        assert_that(compress('MMMMXXX')).is_equal_to('MMMMXXX')

    def test_compressor_does_not_violate_uniqueness_constraint_on_some_characters_when_compressing(self):
        assert_that(compress('LXXXX')).is_equal_to('XC')

    def test_compressor_recurses_if_multiple_substitutions_are_available(self):
        assert_that(compress('XXXXVIIII')).is_equal_to('XLIX')

    def test_compressor_on_arbitrary_input(self):
        assert_that(compress('MCCLXXVIIII')).is_equal_to('MCCLXXIX')


class ConsecutiveOccurrenceTest(unittest.TestCase):
    def test_returns_negative_one_if_string_less_than_n_occurrences(self):
        assert_that(starting_index_of_n_consecutive_occurrences('III', 4)).is_equal_to(-1)

    def test_returns_index_of_start_of_occurrence_if_sequence_contains_consecutive_occurrence(self):
        assert_that(starting_index_of_n_consecutive_occurrences('II', 2)).is_equal_to(0)

    def test_returns_negative_one_if_string_does_not_contain_occurrence(self):
        assert_that(starting_index_of_n_consecutive_occurrences('IVI', 2)).is_equal_to(-1)
