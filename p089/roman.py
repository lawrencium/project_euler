CLASSIC_ROMAN_NUMERAL_HIERARCHY = {
    'I': 'V',
    'V': 'X',
    'X': 'L',
    'L': 'C',
    'C': 'D',
    'D': 'M'

}

MINIMUM_CONSECUTIVE_OCCURRENCE_FOR_COMPRESSION = 4


def starting_index_of_n_consecutive_occurrences(sequence, n):
    if len(sequence) < n:
        return -1

    for index in range(len(sequence) - n + 1):
        value = sequence[index]
        if value == 'M':
            continue

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
        return compress(replace_consecutive_occurrences(consecutive_occurrences_index, roman_numeral))


def replace_consecutive_occurrences(index, roman_numeral):
    def handle_replacement(i, length, replacement):
        return roman_numeral.replace(roman_numeral[i: i + length], replacement, 1)

    def handle_uniqueness_constraint(i, length, replacement):
        return handle_replacement(i, length, replacement)

    repeating_character = roman_numeral[index]
    hierarchical_replacement = CLASSIC_ROMAN_NUMERAL_HIERARCHY[repeating_character]

    if hierarchical_replacement in roman_numeral:
        substring_replacement = repeating_character + CLASSIC_ROMAN_NUMERAL_HIERARCHY[hierarchical_replacement]
        return handle_uniqueness_constraint(index - 1, MINIMUM_CONSECUTIVE_OCCURRENCE_FOR_COMPRESSION + 1,
                                            substring_replacement)
    else:
        substring_replacement = repeating_character + hierarchical_replacement
        return handle_replacement(index, MINIMUM_CONSECUTIVE_OCCURRENCE_FOR_COMPRESSION, substring_replacement)

        # substring_replacement = repeating_character + CLASSIC_ROMAN_NUMERAL_HIERARCHY[
        #     hierarchical_replacement] if hierarchical_replacement in roman_numeral else repeating_character + hierarchical_replacement
        # return roman_numeral.replace(repeating_character * MINIMUM_CONSECUTIVE_OCCURRENCE_FOR_COMPRESSION,
        #                              substring_replacement, 1)
