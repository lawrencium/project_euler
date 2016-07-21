CLASSIC_ROMAN_NUMERAL_HIERARCHY = {
    'I': 'V',
    'X': 'L',
    'C': 'M',
}

MINIMUM_CONSECUTIVE_OCCURRENCE_FOR_COMPRESSION = 4


def starting_index_of_n_consecutive_occurrences(sequence, n):
    if len(sequence) < n:
        return -1

    for index in range(len(sequence) - n + 1):
        value = sequence[index]
        if all([value == sequence[i] for i in range(index + 1, index + n)]):
            return index

    return -1


def compress(roman_numeral):
    if len(roman_numeral) < 4:
        return roman_numeral
    if all([numeral == 'M' for numeral in roman_numeral]):
        return roman_numeral

    consecutive_occurrences_index = starting_index_of_n_consecutive_occurrences(roman_numeral,
                                                                                MINIMUM_CONSECUTIVE_OCCURRENCE_FOR_COMPRESSION)

    if consecutive_occurrences_index == -1:
        return roman_numeral
    else:
        repeating_character = roman_numeral[consecutive_occurrences_index]
        replacement = repeating_character + CLASSIC_ROMAN_NUMERAL_HIERARCHY[repeating_character]
        return roman_numeral.replace(repeating_character * MINIMUM_CONSECUTIVE_OCCURRENCE_FOR_COMPRESSION, replacement,
                                     1)
