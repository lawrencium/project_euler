import math

from util.solutiontimer import time_function

UPPER_BOUND = 10 ** 7
FIRST_REVERSIBLE_NUMBER = 12


def is_even(n):
    return n % 2 == 0


def reverse_number(number):
    number_as_string = str(number)
    reversed_number_as_string = number_as_string[::-1]
    return int(reversed_number_as_string)


def sum_contains_all_odd_digits(n1, n2):
    def check_digits_are_odd(n):
        number_string = str(n)
        for digit_char in number_string:
            if is_even(int(digit_char)):
                return False
        return True

    return check_digits_are_odd(n1 + n2)


def naive_check(n):
    reversed_number = reverse_number(n)
    return sum_contains_all_odd_digits(n, reversed_number)


def pivot_check(n):
    n_string = str(n)
    number_digits = len(n_string)
    if is_even(number_digits):
        raise Exception('Can only check pivot on odd-length numbers. Got {}'.format(n))

    mid_point_index = number_digits / 2

    preceding_digit = int(n_string[mid_point_index - 1])
    succeeding_digit = int(n_string[mid_point_index + 1])

    sum_digits_around_mid_point = preceding_digit + succeeding_digit
    if sum_digits_around_mid_point < 10:
        return False

    ones_place = sum_digits_around_mid_point % 10
    if is_even(ones_place):
        return False

    mid_point = int(n_string[mid_point_index])
    if mid_point * 2 > 10:
        return not is_even(ones_place + 1)

    return True


class ReversibleCounter:
    def __init__(self, upper_bound):
        self._upper_bound = upper_bound

    # noinspection PyMethodMayBeStatic
    def count(self):
        raise Exception('This method needs to be implemented')


class NaiveReversibleCounter(ReversibleCounter):
    def count(self):
        count = 0

        for i in range(FIRST_REVERSIBLE_NUMBER, self._upper_bound):
            if i % 10 == 0:
                continue

            if naive_check(i):
                count += 1

        return count


class SkipNumbersWhereSumHasEvenNumberInOnesPlace(ReversibleCounter):
    def count(self):
        count = 0
        i = FIRST_REVERSIBLE_NUMBER
        group_ceiling = 100
        while i < self._upper_bound:
            if i % 10 == 0:
                i += 2

            if naive_check(i):
                count += 1

            i += 2
            if i >= group_ceiling:
                i += 1
                group_ceiling *= 10

        return count * 2


class GoalPostImplementation(ReversibleCounter):
    def count(self):
        number_intermittent_digits = int(math.log10(self._upper_bound)) - 1

        count = 0
        for number_digits_between_first_and_last_digit in range(number_intermittent_digits):
            for first_digit in range(1, 10):
                for last_digit in range(first_digit + 1, 10, 2):
                    for intermittent_digits in range(10 ** number_digits_between_first_and_last_digit):
                        number_to_check = last_digit + intermittent_digits * 10 + first_digit * 10 ** (
                            number_digits_between_first_and_last_digit + 1)

                        if naive_check(number_to_check):
                            # print number_to_check
                            count += 1
        return count * 2


def main():
    reversible_counter = GoalPostImplementation(UPPER_BOUND)
    reversible_numbers = reversible_counter.count()

    print 'Found {} reversible numbers below {}'.format(reversible_numbers, UPPER_BOUND)


if __name__ == '__main__':
    time_function(main)
