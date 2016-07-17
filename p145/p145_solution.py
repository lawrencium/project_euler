from util.solutiontimer import time_function

UPPER_BOUND = 10 ** 7
FIRST_REVERSIBLE_NUMBER = 12


def reverse_number(number):
    number_as_string = str(number)
    reversed_number_as_string = number_as_string[::-1]
    return int(reversed_number_as_string)


def sum_contains_all_odd_digits(n1, n2):
    def check_digits_are_odd(n):
        number_string = str(n)
        for digit_char in number_string:
            if not int(digit_char) % 2:
                return False
        return True

    return check_digits_are_odd(n1 + n2)


class ReversibleCounter:
    def __init__(self, upper_bound):
        self._upper_bound = upper_bound

    # noinspection PyMethodMayBeStatic
    def count(self):
        raise Exception('This method needs to be implemented')


class NaiveReversibleCounter(ReversibleCounter):
    def count(self):
        def naive_check(n):
            reversed_number = reverse_number(n)
            return sum_contains_all_odd_digits(n, reversed_number)

        count = 0

        for i in range(FIRST_REVERSIBLE_NUMBER, self._upper_bound):
            if i % 10 == 0:
                continue

            if naive_check(i):
                count += 1

        return count


class SkipNumbersWhereSumHasEvenNumberInOnesPlace(ReversibleCounter):
    def count(self):
        def naive_check(n):
            reversed_number = reverse_number(n)
            return sum_contains_all_odd_digits(n, reversed_number)

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


def main():
    reversible_counter = SkipNumbersWhereSumHasEvenNumberInOnesPlace(UPPER_BOUND)
    reversible_numbers = reversible_counter.count()

    print 'Found {} reversible numbers below {}'.format(reversible_numbers, UPPER_BOUND)


if __name__ == '__main__':
    time_function(main)
