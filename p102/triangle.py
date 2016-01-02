from operator import itemgetter

__author__ = 'lawrencechen'


class LineSegmentIntercept:
    def __init__(self):
        pass

    @staticmethod
    def y_intercept(point1, point2):
        point1_x = point1[0]
        point2_x = point2[0]

        if point1_x == point2_x:
            return (-1, -1)

        if point1_x * point2_x > 0:
            return (-1, -1)

        point1_y = point1[1]
        point2_y = point2[1]
        slope = float(point2_y - point1_y) / (point2_x - point1_x)
        intercept = point1_y - slope * point1_x

        return (0, intercept)


class Triangle:
    def __init__(self, vertex1, vertex2, vertex3):
        vertex_list = [vertex1, vertex2, vertex3]

        self._vertices_ordered_by_x_value = sorted(vertex_list, key=itemgetter(0))
        self._vertices_ordered_by_y_value = sorted(vertex_list, key=itemgetter(1))

    def __largest_x_coordinate(self):
        return self._vertices_ordered_by_x_value[2][0]

    def __smallest_x_coordinate(self):
        return self._vertices_ordered_by_x_value[0][0]

    def __largest_y_coordinate(self):
        return self._vertices_ordered_by_y_value[2][1]

    def __smallest_y_coordinate(self):
        return self._vertices_ordered_by_y_value[0][1]

    def overlap_origin(self):
        def valid_y_intercepts():
            intercept = LineSegmentIntercept

            vertices = self._vertices_ordered_by_x_value
            number_vertices = len(vertices)
            intercept_values = set()
            for i in range(number_vertices):
                point1 = vertices[i]
                for j in range(i + 1, number_vertices):
                    point2 = vertices[j]
                    intercept_between_points = intercept.y_intercept(point1, point2)
                    if intercept_between_points[0] == 0:
                        intercept_values.add(intercept_between_points[1])

            if len(intercept_values) == 2:
                return reduce(lambda x, y: x * y, intercept_values) <= 0
            else:
                return False

        if self.__largest_x_coordinate() < 0 or self.__smallest_x_coordinate() > 0:
            return False

        if self.__largest_y_coordinate() < 0 or self.__smallest_y_coordinate() > 0:
            return False

        return valid_y_intercepts()
