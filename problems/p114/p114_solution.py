from problems.util.solutiontimer import time_function


class NumberTilingOptions(object):
    def __init__(self, ending_in_black, ending_in_red):
        self.black = ending_in_black
        self.red = ending_in_red

    def total(self):
        return self.black + self.red


def main():
    number_tiles = 50
    number_tiling_options_for = [None for _ in range(number_tiles)]

    number_tiling_options_for[0] = NumberTilingOptions(1, 0)
    number_tiling_options_for[1] = NumberTilingOptions(1, 0)
    number_tiling_options_for[2] = NumberTilingOptions(1, 1)

    for i in range(3, number_tiles):
        previous = number_tiling_options_for[i - 1]
        options_ending_in_black = previous.black + previous.red
        options_ending_in_red = 1 + sum([number_tiling_options_for[j].black for j in range(i - 2)])
        number_tiling_options_for[i] = NumberTilingOptions(options_ending_in_black, options_ending_in_red)

    print number_tiling_options_for[-1].total()


if __name__ == '__main__':
    time_function(main)
