from problems.util.solutiontimer import time_function


def main():
    stopping_condition = 5
    permutation_tracker = PermutationTracker(stopping_condition)
    start = 1
    i = start
    while True:
        to_insert = i ** 3

        condition_met = permutation_tracker.insert(to_insert)
        if condition_met:
            print 'Found {} cubic permutations with the lowest cube being {}'.format(stopping_condition, condition_met)
            return
        i += 1


class PermutationTrackingInformation(object):
    def __init__(self, count, number):
        self.count = count
        self.number = number


class PermutationTracker(object):
    def __init__(self, stopping_condition):
        self.__stopping_condition = stopping_condition
        self.__permutation_map = {}

    def insert(self, number):
        number_sorted = ''.join(sorted(str(number)))
        permutation_tracking_information = self.__permutation_map.setdefault(number_sorted,
                                                                             PermutationTrackingInformation(0, number))
        permutation_tracking_information.count += 1
        self.__permutation_map[number_sorted] = permutation_tracking_information

        if self.__permutation_map[number_sorted].count == self.__stopping_condition:
            return self.__permutation_map[number_sorted].number


if __name__ == '__main__':
    time_function(main)
