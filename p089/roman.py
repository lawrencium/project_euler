CLASSIC_ROMAN_NUMERAL_MAPPING = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 20,
    'C': 100,
    'D': 500,
    'M': 1000
}


class RomanNumeralTransformer(object):
    def __init__(self, mapping):
        self._mapping = mapping

    def to_arabic_representation(self, roman_numeral):
        return self._mapping[roman_numeral]
