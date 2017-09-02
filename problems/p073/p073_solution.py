import math

from problems.util.solutiontimer import time_function

lower_bound = float(1) / 3
upper_bound = float(1) / 2
d = 12000


# d = 8


def get_lower_bounded_numerator(denominator):
    unfloored_numerator = lower_bound * denominator
    floored = math.ceil(unfloored_numerator)
    return floored + 1 if unfloored_numerator == floored else floored


def get_upper_bounded_numerator(denominator):
    unfloored_numerator = upper_bound * denominator
    floored = math.floor(unfloored_numerator)
    return floored - 1 if unfloored_numerator == floored else floored


def main():
    set_of_reduced_fractions = set()
    for denominator in range(4, d + 1):
        lower_bound_numerator = int(get_lower_bounded_numerator(denominator))
        upper_bound_numerator = int(get_upper_bounded_numerator(denominator))
        [set_of_reduced_fractions.add(float(i) / denominator) for i in
         range(lower_bound_numerator, upper_bound_numerator + 1)]

    print len(set_of_reduced_fractions)


if __name__ == '__main__':
    time_function(main)
