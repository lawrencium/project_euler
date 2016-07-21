import unittest

from assertpy import assert_that

from p089.roman import RomanNumeralTransformer, CLASSIC_ROMAN_NUMERAL_MAPPING


class ArabicTransformationTest(unittest.TestCase):
    def setUp(self):
        self.transformer = RomanNumeralTransformer(CLASSIC_ROMAN_NUMERAL_MAPPING)

    def test_transformer_returns_correct_integer_for_single_character_roman_numeral(self):
        assert_that(self.transformer.to_arabic_representation('I')).is_equal_to(1)

    def test_transformer_returns_correct_integer_for_multiple_chracter_numeral_with_no_subtraction(self):
        assert_that(self.transformer.to_arabic_representation('XVI')).is_equal_to(16)
