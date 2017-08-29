import math

from problems.util.prime import sieve_of_eratosthenes
from problems.util.solutiontimer import time_function

element_to_find = float(3) / 7
d = 1000000
sieve = sieve_of_eratosthenes(d)


def calculate_numerator():
    closest_decimal = (1, 3)
    distance = element_to_find - float(1) / 3
    for denominator in range(4, d + 1):
        unfloored_numerator = element_to_find * denominator
        floored = math.floor(unfloored_numerator)
        adjusted_numerator = floored - 1 if unfloored_numerator == floored else floored

        as_decimal = adjusted_numerator / denominator
        distance_between_decimal_and_element = element_to_find - as_decimal

        if distance_between_decimal_and_element < distance:
            distance = distance_between_decimal_and_element
            closest_decimal = (adjusted_numerator, denominator)

    print 'Element to the left of 3/7 is {}'.format(closest_decimal)


if __name__ == '__main__':
    time_function(calculate_numerator)
