from p102.triangle import Triangle
from util import filereader
from util.solutiontimer import time_function

__author__ = 'lawrencechen'


def main():
    triangles_file = filereader.read_file('p102_triangles.txt')
    number_overlapping_triangles = 0
    for triangle_string in triangles_file:
        coordinates = map(lambda x: int(x), triangle_string.split(','))
        vertex1 = (coordinates[0], coordinates[1])
        vertex2 = (coordinates[2], coordinates[3])
        vertex3 = (coordinates[4], coordinates[5])

        triangle = Triangle(vertex1, vertex2, vertex3)
        if triangle.overlap_origin():
            number_overlapping_triangles += 1
    print number_overlapping_triangles


if __name__ == '__main__':
    time_function(main)
