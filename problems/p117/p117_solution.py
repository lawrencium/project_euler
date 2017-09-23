from problems.util.solutiontimer import time_function

red_tile_length = 2
green_tile_length = 3
blue_tile_length = 4


def main():
    number_tiles = 50
    number_tiling_options = [0 for _ in range(number_tiles)]

    number_tiling_options[1] = 1
    number_tiling_options[2] = 3
    number_tiling_options[3] = 7

    for i in range(4, number_tiles):
        ith_tile_unused = number_tiling_options[i - 1]
        ith_tile_is_red = number_tiling_options[i - 2] + 1
        ith_tile_is_green = number_tiling_options[i - 3] + 1
        ith_tile_is_blue = number_tiling_options[i - 4] + 1
        total_sum = ith_tile_unused + ith_tile_is_red + ith_tile_is_green + ith_tile_is_blue
        number_tiling_options[i] = total_sum

    print number_tiling_options[-1] + 1


if __name__ == '__main__':
    time_function(main)
