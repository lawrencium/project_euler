from copy import deepcopy
from operator import attrgetter

__author__ = 'lawrencechen'


class InsertInformation(object):
    def __init__(self, number, asterisk_value):
        self._asterisk_value = asterisk_value
        self._number = number

        number_string = str(number)
        self._string_pattern = number_string.replace(asterisk_value, '*') if asterisk_value else number_string

        self.__current_level = 0

    @property
    def next_digit(self):
        digit = self._string_pattern[self.__current_level]
        self.__current_level += 1
        return digit

    @property
    def asterisk_value(self):
        return self._asterisk_value

    @property
    def number(self):
        return self._number

    def child_is_leaf(self):
        return self.__current_level == len(self._string_pattern) - 1


class PrimeNode(object):
    def __init__(self):
        self.digits = {}

    def insert(self, insert_information):
        pass


class FamilyInformation(object):
    def __init__(self, smallest_value):
        self._smallest_value = smallest_value
        self._count = 1

    @property
    def smallest_value(self):
        return self._smallest_value

    @property
    def count(self):
        return self._count

    def increment(self):
        self._count += 1


class PrimeLeafNode(PrimeNode):
    def insert(self, insert_information):
        digit = insert_information.next_digit
        number = insert_information.number
        family_information = self.__increment_value(digit, number)

        if digit == '*':
            alternative = self.__increment_value(insert_information.asterisk_value, number)
            if alternative.count > family_information.count:
                family_information = alternative

        return family_information

    def __increment_value(self, digit, number):
        if digit in self.digits:
            information = self.digits[digit]
            information.increment()
        else:
            self.digits[digit] = FamilyInformation(number)

        return self.digits[digit]


class PrimeIndexNode(PrimeNode):
    def insert(self, insert_information):
        digit = insert_information.next_digit
        next_level_is_leaf = insert_information.child_is_leaf()

        insert_information_deep_copy = deepcopy(insert_information)
        child = self.__child(digit, next_level_is_leaf)
        family = child.insert(insert_information)

        if digit == '*':
            alternative_child = self.__child(insert_information.asterisk_value, next_level_is_leaf)
            alternative_family = alternative_child.insert(insert_information_deep_copy)
            if alternative_family.count > family.count:
                family = alternative_family

        return family

    def __child(self, digit, next_level_is_leaf):
        if digit in self.digits:
            return self.digits[digit]
        else:
            child = PrimeLeafNode() if next_level_is_leaf else PrimeIndexNode()
            self.digits[digit] = child
            return child


class PrimeDigitTrie(object):
    def __init__(self, levels):
        self._levels = levels
        self._root = PrimeLeafNode() if levels == 1 else PrimeIndexNode()

    def insert(self, value):
        def duplicates(n):
            n_string = str(n)
            return set([x for x in n_string if n_string.count(x) > 1])

        if value <= 0:
            raise Exception('Cannot insert non-zero value')

        number_digits = len(str(value))
        if number_digits != self._levels:
            raise Exception('Trying to insert number with %i digits into %i level tree' % (number_digits, self._levels))

        dups = duplicates(value)
        if dups:
            families = [self._root.insert(InsertInformation(value, dup)) for dup in dups]
            return max(families, key=attrgetter('smallest_value'))
        else:
            return self._root.insert(InsertInformation(value, ''))
