__author__ = 'lawrencechen'


def read_file(filename):
    result = []
    with open(filename) as f:
        for line in f:
            result.append(line)
    return result
