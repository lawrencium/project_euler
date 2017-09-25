class NumberTilingOptions(object):
    def __init__(self, ending_in_black, ending_in_red):
        self.black = ending_in_black
        self.red = ending_in_red

    def total(self):
        return self.black + self.red


class BlockCombinationCounter(object):
    def __init__(self, m, n):
        self.minimum_red_length = m
        self.row_length = n

    def count(self):
        number_tiling_options_for = [NumberTilingOptions(1, 0) for _ in range(self.row_length)]

        number_tiling_options_for[self.minimum_red_length - 1] = NumberTilingOptions(1, 1)
        for i in range(self.minimum_red_length, self.row_length):
            previous = number_tiling_options_for[i - 1]
            options_ending_in_black = previous.black + previous.red
            range_of_ending_black_tiles = range(i - (self.minimum_red_length - 1))
            options_ending_in_red = 1 + sum([number_tiling_options_for[j].black for j in range_of_ending_black_tiles])
            number_tiling_options_for[i] = NumberTilingOptions(options_ending_in_black, options_ending_in_red)

        return number_tiling_options_for[-1].total()
