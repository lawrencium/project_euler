from problems.util.solutiontimer import time_function

UPPER_BOUND = 10 ** 4 - 1
TRIANGLE_TAG = 1
SQUARE_TAG = 2
PENTAGONAL_TAG = 3
HEXAGONAL_TAG = 4
HEPTAGONAL_TAG = 5
OCTAGONAL_TAG = 6


def triangle_number(n):
    return n * (n + 1) / 2


def square_number(n):
    return n ** 2


def pentagonal_number(n):
    return n * (3 * n - 1) / 2


def hexagonal_number(n):
    return n * (2 * n - 1)


def heptagonal_number(n):
    return n * (5 * n - 3) / 2


def octagonal_number(n):
    return n * (3 * n - 2)


def generate_polygonal_series(f, limit):
    series = []

    n = 1
    member = f(n)
    while member < limit:
        series.append(member)

        n += 1
        member = f(n)

    series = filter(lambda x: x >= 1000, series)
    return set(series)


def build_transition_table(numbers):
    transition_table = {}
    for polygonal in numbers:
        last_two_digits = get_last_two_digits(polygonal)
        if last_two_digits in transition_table:
            continue
        if last_two_digits[0] == '0':
            continue

        transition_numbers = set(
            [i for i in numbers if get_first_two_digits(i) == last_two_digits and get_last_two_digits(i)[0] != '0'])
        transition_table[last_two_digits] = transition_numbers

    return transition_table


def get_last_two_digits(n):
    return str(n)[-2:]


def get_first_two_digits(n):
    return str(n)[:2]


def find_cycle_candidates(starting_series, transition_table):
    cycle_candidates = []
    for candidate1 in starting_series:
        possible_transitions1 = transition_table[get_last_two_digits(candidate1)]
        for candidate2 in possible_transitions1:
            possible_transitions2 = transition_table[get_last_two_digits(candidate2)]
            for candidate3 in possible_transitions2:
                possible_transitions3 = transition_table[get_last_two_digits(candidate3)]
                for candidate4 in possible_transitions3:
                    possible_transitions4 = transition_table[get_last_two_digits(candidate4)]
                    for candidate5 in possible_transitions4:
                        possible_transitions5 = transition_table[get_last_two_digits(candidate5)]
                        for candidate6 in possible_transitions5:
                            if get_last_two_digits(candidate6) == get_first_two_digits(candidate1):
                                cycle_candidates.append(
                                    [candidate1, candidate2, candidate3, candidate4, candidate5, candidate6])
    return cycle_candidates


def generate_tag_table(heptagonal_series, hexagonal_series, octagonal_series, pentagonal_series, square_series,
                       triangle_series):
    def augment_tag_table(table, series):
        numbers, tag = series

        for number in numbers:
            if number in table:
                table[number].append(tag)
            else:
                table[number] = [tag]

    tag_table = {}
    augment_tag_table(tag_table, triangle_series)
    augment_tag_table(tag_table, square_series)
    augment_tag_table(tag_table, pentagonal_series)
    augment_tag_table(tag_table, hexagonal_series)
    augment_tag_table(tag_table, heptagonal_series)
    augment_tag_table(tag_table, octagonal_series)

    return tag_table


def contains_all_polygonal_types(candidate, tag_table):
    sorted_tag_ordering = [TRIANGLE_TAG, SQUARE_TAG, PENTAGONAL_TAG, HEXAGONAL_TAG, HEPTAGONAL_TAG, OCTAGONAL_TAG]

    def recursive_checker(remaining_candidates, observed_tags):
        if remaining_candidates:
            polygonal_number = remaining_candidates[0]
            types = tag_table[polygonal_number]
            for t in types:
                if t in observed_tags:
                    continue
                if recursive_checker(remaining_candidates[1:], observed_tags + [t]):
                    return True
            return False
        else:
            return sorted(observed_tags) == sorted_tag_ordering

    return recursive_checker(candidate, [])


def find_cycle_with_all_polygonal_types(cycle_candidates, tag_table):
    for candidate in cycle_candidates:
        if contains_all_polygonal_types(candidate, tag_table):
            return candidate
    raise Exception('contains_all_polygonal_types() does not work because could not identify a valid cycle')


def main():
    triangle_series = generate_polygonal_series(triangle_number, UPPER_BOUND), TRIANGLE_TAG
    square_series = generate_polygonal_series(square_number, UPPER_BOUND), SQUARE_TAG
    pentagonal_series = generate_polygonal_series(pentagonal_number, UPPER_BOUND), PENTAGONAL_TAG
    hexagonal_series = generate_polygonal_series(hexagonal_number, UPPER_BOUND), HEXAGONAL_TAG
    heptagonal_series = generate_polygonal_series(heptagonal_number, UPPER_BOUND), HEPTAGONAL_TAG
    octagonal_series = generate_polygonal_series(octagonal_number, UPPER_BOUND), OCTAGONAL_TAG

    tag_table = generate_tag_table(heptagonal_series, hexagonal_series, octagonal_series, pentagonal_series,
                                   square_series, triangle_series)

    all_polygonal_numbers = (triangle_series[0] | square_series[0] | pentagonal_series[0] | hexagonal_series[0] |
                             heptagonal_series[0] | octagonal_series[0])

    transition_table = build_transition_table(all_polygonal_numbers)

    octagonal_series_filtered = filter(lambda x: get_last_two_digits(x)[0] != '0', octagonal_series[0])
    cycle_candidates = find_cycle_candidates(octagonal_series_filtered, transition_table)

    cycle = find_cycle_with_all_polygonal_types(cycle_candidates, tag_table)

    print 'Found cycle :: {} which has sum {}'.format(cycle, sum(cycle))


if __name__ == '__main__':
    time_function(main)
