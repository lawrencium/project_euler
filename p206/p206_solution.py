from util.solutiontimer import time_function

CONCEALED_SQUARE_LENGTH = 19
CONCEALED_SQUARE = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def is_concealed_square(x):
    square = x ** 2
    square_string = str(square)

    if len(square_string) != CONCEALED_SQUARE_LENGTH:
        raise Exception('Square out of bounds')

    return [square_string[i] for i in range(0, len(square_string), 2)] == CONCEALED_SQUARE


def main():
    x = 1000000000

    while not is_concealed_square(x):
        x += 10

    print 'Found a concealed square :', x


if __name__ == '__main__':
    time_function(main)
