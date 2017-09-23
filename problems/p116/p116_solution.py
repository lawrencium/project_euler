from problems.util.solutiontimer import time_function


def main():
    print tiling_options_for_red(50) + tiling_options_for_blue(50) + tiling_options_for_green(50)


def tiling_options_for_red(number_tiles):
    return tiling_options_for(number_tiles, 2)


def tiling_options_for_green(number_tiles):
    return tiling_options_for(number_tiles, 3)


def tiling_options_for_blue(number_tiles):
    return tiling_options_for(number_tiles, 4)


def tiling_options_for(number_tiles, replacement_tile_length):
    number_tiling_options = [0 for _ in range(number_tiles)]
    number_tiling_options[replacement_tile_length - 1] = 1

    for i in range(replacement_tile_length, number_tiles):
        number_tiling_options[i] = number_tiling_options[i - 1] + number_tiling_options[i - replacement_tile_length] + 1

    return number_tiling_options[-1]


if __name__ == '__main__':
    time_function(main)
