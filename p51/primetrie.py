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


class PrimeNode(object):
    def __init__(self):
        self.digits = {}

    def insert(self, number):
        pass


class PrimeLeafNode(PrimeNode):
    class Information(object):
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

    def insert(self, insert_information):
        digit = insert_information.next_digit
        number = insert_information.number
        information = self.__increment_value(digit, number)

        if digit == '*':
            alternative = self.__increment_value(insert_information.asterisk_value, number)
            if alternative.count > information.count:
                information = alternative

        return information

    def __increment_value(self, digit, number):
        if digit in self.digits:
            information = self.digits[digit]
            information.increment()
        else:
            self.digits[digit] = PrimeLeafNode.Information(number)

        return self.digits[digit]


class PrimeIndexNode(PrimeNode):
    def __init__(self):
        super(PrimeIndexNode, self).__init__()


class PrimeDigitTrie(object):
    def __init__(self, levels):
        self._levels = levels
        self._root = PrimeLeafNode() if levels == 1 else PrimeIndexNode()

    def insert(self, value):
        if value <= 0:
            raise Exception('Cannot insert non-zero value')

        number_digits = len(str(value))
        if number_digits != self._levels:
            raise Exception('Trying to insert number with %i digits into %i level tree' % (number_digits, self._levels))
