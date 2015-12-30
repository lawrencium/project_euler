import util

# Grid 07
matrix = "043080250600000000000001094900004070000608000010200003820500000000000005034090710"

# Grid 48
matrix = "001007090590080001030000080000005800050060020004100000080000030100020079020700400"

# test case
matrix = ".........76...3..2..264...94.39...7......49.3..5....2..1.56....37..9..41.......6.".replace('.', '0')

matrix = '080750000506400000070006080800009000960007810007100000620900008795800006408675920'

class SudokuCell(object):
    """ represents a sudoku cell """
    BOX1 = 1
    BOX2 = 2
    BOX3 = 3
    BOX4 = 4
    BOX5 = 5
    BOX6 = 6
    BOX7 = 7
    BOX8 = 8
    BOX9 = 9

    @staticmethod
    def get_box_num(row, col):
        if row < 3:
            if col < 3:
                return SudokuValue.BOX1
            elif col < 6:
                return SudokuValue.BOX2
            else:  # col is (6..8)
                return SudokuValue.BOX3
        elif row < 6:
            if col < 3:
                return SudokuValue.BOX4
            elif col < 6:
                return SudokuValue.BOX5
            else:  # col is (6..8)
                return SudokuValue.BOX6
        else:  # row is (6..8)
            if col < 3:
                return SudokuValue.BOX7
            elif col < 6:
                return SudokuValue.BOX8
            else:  # col is (6..8)
                return SudokuValue.BOX9

class SudokuValue(SudokuCell):
    """ represents a SudokuCell with a definite value """
    def __init__(self, val):
        self._value = val

    def value():
        doc = "The value property."
        def fget(self):
            return self._value
        return locals()
    value = property(**value())

class SudokuPossibilities(SudokuCell):
    """ represents a SudokuCell with a list of possible values, initialized from [1..9] """
    def __init__(self, row, col):
        self._possible_values = [i for i in range(1, 10)]
        self._box_num = SudokuCell.get_box_num(row, col)

    def possible_values():
        doc = "The possible_values property."
        def fget(self):
            return self._possible_values
        def fset(self, x):
            self._possible_values = x
        return locals()
    possible_values = property(**possible_values())

    def box_num():
        doc = "The box_num property."
        def fget(self):
            return self._box_num
        return locals()
    box_num = property(**box_num())

    def remove_elem(self, val):
        self._possible_values[:] = [i for i in self._possible_values if i != val]

def get_init_group_ind(n):
    return n / 3 * 3

def sum_top_left(sudoku_matrix):
    place = 100
    num = 0
    for i in range(3):
        num += place * sudoku_matrix[0][i].value
        place /= 10
    return num

def matrix_is_valid(sudoku_matrix):
    """ checks if sudoku_matrix is a valid sudoku result """
    HOUSE = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    def row_is_valid(row):
        """ checks if row `row` is valid """
        sudoku_row = sudoku_matrix[row]
        sudoku_row_vals = [i.value for i in sudoku_row]
        return sorted(sudoku_row_vals) == HOUSE
    def col_is_valid(col):
        sudoku_col = [sudoku_matrix[r][col] for r in range(len(sudoku_matrix))]
        sudoku_row_vals = [i.value for i in sudoku_col]
        return sorted(sudoku_row_vals) == HOUSE
    def box_is_valid(row, col):
        row_ind = get_init_group_ind(row)
        col_ind = get_init_group_ind(col)
        row_range, col_range = range(row_ind, row_ind + 3), range(col_ind, col_ind + 3)
        sudoku_vals = []
        for r in row_range:
            for c in col_range:
                sudoku_vals.append(sudoku_matrix[r][c].value)
        return sorted(sudoku_vals) == HOUSE

    if count_uncertain_values(sudoku_matrix):  # puzzle is unsolved
        return False

    # check rows and cols
    for i in range(len(sudoku_matrix)):
        if not (row_is_valid(i) and col_is_valid(i)):
            return False

    # check boxes
    for r in range(3):
        for c in range(3):
            row, col = r*3, c*3
            if not box_is_valid(row, col):
                return False
    return True

def matrix_to_string(sudoku_matrix):
    """ prints a matrix of SudokuCells in readable format """
    matrix_string = [' ---' * 6]
    matrix_string.append('\n')
    row_count = 1
    col_count = 1
    for row in sudoku_matrix:
        matrix_string.append('| ')
        for cell in row:
            if isinstance(cell, SudokuValue):
                matrix_string.append('%i ' % cell.value)
            else:
                matrix_string.append('X ')
            if col_count % 3 == 0:
                matrix_string.append('| ')
            col_count += 1
        matrix_string.append('\n')
        if row_count % 3 == 0:
            matrix_string.append(' ---' * 6)
            matrix_string.append('\n')
        row_count += 1
    return ''.join(matrix_string)

def convert_matrix(matrix):
    """ converts 2-D int array to 2-D array of Sudoku possibilities """
    sudoku_matrix = [[0 for i in range(9)] for j in range(9)]

    iterator = iter(matrix)
    # fill sudoku_matrix
    for i in range(len(sudoku_matrix)):
        for j in range(len(sudoku_matrix)):
            next_val = int(next(iterator))
            sudoku_matrix[i][j] = SudokuValue(next_val) if next_val else SudokuPossibilities(i , j)
    return sudoku_matrix

def count_uncertain_values(matrix):
    """ counts num of SudokuPossibilities in matrix """
    cnt = 0
    for row in matrix:
        for value in row:
            if isinstance(value, SudokuPossibilities):
                cnt += 1
    return cnt

def count_num_possibilities(matrix):
    """ counts cumulative num of possibilities for all SudokuPossibilities in matrix """
    cnt = 0
    for row in matrix:
        for value in row:
            # print type(value)
            if isinstance(value, SudokuPossibilities):
                cnt += len(value.possible_values)
    return cnt

def get_box_vals(sudoku_matrix, row, col):
    """ get all SudokuValues in box associated with row, col """
    row_ind_start = get_init_group_ind(row)
    col_ind_start = get_init_group_ind(col)
    box_row_range = range(row_ind_start, row_ind_start + 3)
    box_col_range = range(col_ind_start, col_ind_start + 3)

    vs = []
    for r in box_row_range:
        for c in box_col_range:
            cell = sudoku_matrix[r][c]
            if isinstance(cell, SudokuValue):
                vs.append(cell.value)
    return vs

def get_col_vals(sudoku_matrix, row, col):
    """ get all SudokuValues associated with col """
    vs = []
    for r in sudoku_matrix:
        if isinstance(r[col], SudokuValue):
            vs.append(r[col].value)
    return vs

def get_row_vals(sudoku_matrix, row, col):
    """ get all values associated with row """
    return [cell.value for cell in sudoku_matrix[row] if isinstance(cell, SudokuValue)]

def get_surrounding_values(sudoku_matrix, row, col):
    """ returns all values associated with row, col (row, col, and box) """
    row_vals = get_row_vals(sudoku_matrix, row, col)
    col_vals = get_col_vals(sudoku_matrix, row, col)
    box_vals = get_box_vals(sudoku_matrix, row, col)
    return list(set(col_vals + row_vals + box_vals))

def set_value_in_matrix(sudoku_matrix, row, col, value):
    sudoku_matrix[row][col] = SudokuValue(value)
    remove_possibility_from_row(sudoku_matrix, row, value)
    remove_possibility_from_col(sudoku_matrix, col, value)
    remove_possibility_from_box(sudoku_matrix, row, col, value)

def sudoku(matrix):
    sudoku_matrix = convert_matrix(matrix)

    while True:
        num_possibilities_beginning = count_num_possibilities(sudoku_matrix)
        sudoku_matrix = naked_single(sudoku_matrix)
        sudoku_matrix = hidden_single(sudoku_matrix)
        sudoku_matrix = scan_possible_values(sudoku_matrix)
        sudoku_matrix = find_subsets(sudoku_matrix)
        sudoku_matrix = x_wing(sudoku_matrix)

        num_possibilities = count_num_possibilities(sudoku_matrix)
        if not num_possibilities:  # puzzle solved
            break
        elif num_possibilities_beginning == num_possibilities:
            print "Could not completely solve sudoku puzzle using current methods."
            return sudoku_matrix

    if matrix_is_valid(sudoku_matrix):
        return sudoku_matrix
    else:
        print matrix_to_string(sudoku_matrix)
        raise Exception('Outputted sudoku soution contains error')

def x_wing(sudoku_matrix):
    def reverse_dict(d):
        reverse_d = {}
        for k in d:
            vs = d[k]
            for v in vs:
                if v in reverse_d:
                    reverse_d[v].append(k)
                else:
                    reverse_d[v] = [k]
        return reverse_d
    def get_possible_values_in_row(row):
        l = {}
        for col in range(9):
            # print row, col
            if isinstance(sudoku_matrix[row][col], SudokuPossibilities):
                l[col] = sudoku_matrix[row][col].possible_values
        # print l
        return l
    def get_possible_values_in_col(col):
        l = {}
        for row in range(9):
            if isinstance(sudoku_matrix[row][col], SudokuPossibilities):
                l[row] = sudoku_matrix[row][col].possible_values
        return l

    def check_rows():
        for row1 in range(9):
            # row1_possibilities gives dict; k=row index, v=possible values
            row1_possibilities = get_possible_values_in_row(row1)
            if not row1_possibilities:
                continue
            # row1_possibilities_inds gives dict; k=possible value, v=row_inds where len(v)==2
            row1_possibilities_inds = {k:v for (k, v) in reverse_dict(row1_possibilities).items() if len(v) == 2}
            for row2 in range(row1 + 1, 9):
                row2_possibilities = get_possible_values_in_row(row2)
                if not row2_possibilities:
                    continue
                row2_possibilities_inds = {k:v for (k, v) in reverse_dict(row2_possibilities).items() if len(v) == 2}
                # print 'rows', row1, row2
                # print row1_possibilities, row2_possibilities
                possible_x_wings = util.set_intersection(row2_possibilities_inds.keys(), row1_possibilities_inds.keys())
                if possible_x_wings:  # there are potential x_wing vals
                    # check indexes
                    for potential_x_wing in possible_x_wings:
                        if row1_possibilities_inds[potential_x_wing] == row2_possibilities_inds[potential_x_wing]:
                            # matching indexes --> found a x-wing
                            # remove val from both cols
                            rows_to_ignore = [row1, row2]
                            col1, col2 = row1_possibilities_inds[potential_x_wing]
                            remove_possibility_from_col(sudoku_matrix, col1, potential_x_wing, rows_to_ignore)
                            remove_possibility_from_col(sudoku_matrix, col2, potential_x_wing, rows_to_ignore)
    def check_cols():
        for col1 in range(9):
            col1_possibilities = get_possible_values_in_col(col1)
            if not col1_possibilities:
                continue
            col1_possibilities_inds = {k:v for (k, v) in reverse_dict(col1_possibilities).items() if len(v) == 2}
            for col2 in range(col1+1, 9):
                col2_possibilities = get_possible_values_in_col(col2)
                if not col2_possibilities:
                    continue
                col2_possibilities_inds = {k:v for (k, v) in reverse_dict(col2_possibilities).items() if len(v) == 2}
                possible_x_wings = util.set_intersection(col2_possibilities_inds.keys(), col1_possibilities_inds.keys())
                if possible_x_wings:
                    for potential_x_wing in possible_x_wings:
                        if col1_possibilities_inds[potential_x_wing] == col2_possibilities_inds[potential_x_wing]:
                            cols_to_ignore = [col1, col2]
                            row1, row2 = col1_possibilities_inds[potential_x_wing]
                            remove_possibility_from_row(sudoku_matrix, row1, potential_x_wing, cols_to_ignore)
                            remove_possibility_from_row(sudoku_matrix, row2, potential_x_wing, cols_to_ignore)


    check_rows()
    check_cols()
    return sudoku_matrix

def scan_possible_values(sudoku_matrix):
    for box_row in range(3):
        for box_col in range(3):
            box_row_range = range(3*box_row, 3*box_row + 3)
            box_col_range = range(3*box_col, 3*box_col + 3)
            box_vals = get_box_vals(sudoku_matrix, 3*box_row, 3*box_col)
            test_vals = [i for i in range(1, 10) if i not in box_vals]
            for test_val in test_vals:
                rows_with_test_val = []
                cols_with_test_val = []
                for row in box_row_range:
                    for col in box_col_range:
                        sudoku_cell = sudoku_matrix[row][col]
                        if isinstance(sudoku_cell, SudokuPossibilities):
                            if len(sudoku_cell.possible_values) == 1:
                                value = sudoku_cell.possible_values[0]
                                set_value_in_matrix(sudoku_matrix, row, col, value)
                                # print 'setting (%i,%i) = %i (found while scanning)' %(row, col, sudoku_cell.possible_values[0])
                                # print matrix_to_string(sudoku_matrix)
                                # remove value from all associated possibilities
                                continue
                            else:
                                if test_val in sudoku_cell.possible_values:
                                    if not row in rows_with_test_val:
                                        rows_with_test_val.append(row)
                                    if not col in cols_with_test_val:
                                        cols_with_test_val.append(col)
                if test_val in get_box_vals(sudoku_matrix, 3*box_row, 3*box_col):
                    # value has alraedy been added to the box in a previous iteration of the for loop
                    continue
                if len(rows_with_test_val) == 1:  # found a pointing pair in row
                    # print test_val
                    row = rows_with_test_val[0]
                    if len(cols_with_test_val) == 1:  # even better -> found only 1 col value will fit
                        col = cols_with_test_val[0]
                        set_value_in_matrix(sudoku_matrix, row, col, test_val)
                        # print 'setting (%i,%i) = %i (pointing pair)' %(row, col, test_val)
                        # print matrix_to_string(sudoku_matrix)
                    col_range = range(get_init_group_ind(col), get_init_group_ind(col) + 3)
                    # remove testval from possibilities in row
                    remove_possibility_from_row(sudoku_matrix, row, test_val, col=col_range)
                elif len(cols_with_test_val) == 1:  # found a pointing pair in col
                    col = cols_with_test_val[0]
                    row_range = range(get_init_group_ind(row), get_init_group_ind(row) + 3)
                    # remove testval from possibilities in col
                    remove_possibility_from_col(sudoku_matrix, col, test_val, row=row_range)
    return sudoku_matrix

def find_subsets(sudoku_matrix):
    def powerset(l, size):
        """ returns set of powerset of l where size of every subset is == min_size """
        return filter(lambda x: len(x) == size, util.power_set(l))

    def get_num_occurrences(l):
        count_dict = {}
        for i in range(1, 10):  # fill count_dict
            count_dict[i] = 0
        for cell_possibilities in l:
            for possibility in cell_possibilities:
                count_dict[possibility] += 1
        return count_dict

    def occurrence_inds(occurrence, candidate_list):
        inds = []
        for i in candidate_list:
            possibilities_at_i = candidate_list[i]
            if occurrence in possibilities_at_i:
                inds.append(i)
        return inds

    def get_row_candidates(row):
        l = {}
        for c in range(len(sudoku_matrix)):
            sudoku_cell = sudoku_matrix[row][c]
            if isinstance(sudoku_cell, SudokuPossibilities):
                l[c] = sudoku_cell.possible_values
        return l
    def get_col_candidates(col):
        l = {}
        for r in range(len(sudoku_matrix)):
            sudoku_cell = sudoku_matrix[r][col]
            if isinstance(sudoku_cell, SudokuPossibilities):
                l[r] = sudoku_cell.possible_values
        return l
    def get_box_candidates(row, col):
        l = {}
        row_ind = get_init_group_ind(row)
        col_ind = get_init_group_ind(col)
        for r in range(row_ind, row_ind + 3):
            for c in range(col_ind, col_ind + 3):
                sudoku_cell = sudoku_matrix[r][c]
                if isinstance(sudoku_cell, SudokuPossibilities):
                    l[r, c] = sudoku_cell.possible_values
        return l

    def check_rows_naked(subset_size):
        def check_row(row):
            row_candidates = get_row_candidates(row)
            all_possibilities_in_row = list(set([item for sublist in row_candidates.values() for item in sublist]))
            subsets_to_check = powerset(all_possibilities_in_row, subset_size)
            for subset in subsets_to_check:
                num_naked = 0
                for possibility in row_candidates.values():
                    difference = util.set_subtraction(possibility, subset)
                    if not difference:  # element is member of naked set
                        num_naked += 1
                if num_naked == subset_size:  # subset is a naked set
                    for col in row_candidates:
                        sudoku_cell = sudoku_matrix[row][col]
                        difference = util.set_subtraction(sudoku_cell.possible_values, subset)
                        if difference:  # sudoku_cell is not member of naked set --> set possible_values
                            sudoku_cell.possible_values = difference
        for row in range(len(sudoku_matrix)):
            check_row(row)

    def check_cols_naked(subset_size):
        def check_col(col):
            col_candidates = get_col_candidates(col)
            all_possibilities_in_col = list(set([item for sublist in col_candidates.values() for item in sublist]))
            subsets_to_check = powerset(all_possibilities_in_col, subset_size)
            for subset in subsets_to_check:
                num_naked = 0
                for possibility in col_candidates.values():
                    difference = util.set_subtraction(possibility, subset)
                    if not difference:
                        num_naked += 1
                if num_naked == subset_size:
                    for row in col_candidates:
                        sudoku_cell = sudoku_matrix[row][col]
                        difference = util.set_subtraction(sudoku_cell.possible_values, subset)
                        if difference:
                            sudoku_cell.possible_values = difference
        for col in range(len(sudoku_matrix)):
            check_col(col)

    def check_boxes_naked(subset_size):
        def check_box(row, col):
            box_candidates = get_box_candidates(row, col)
            all_possibilities_in_box = list(set([item for sublist in box_candidates.values() for item in sublist]))
            subsets_to_check = powerset(all_possibilities_in_box, subset_size)
            for subset in subsets_to_check:
                num_naked = 0
                for possibility in box_candidates.values():
                    difference = util.set_subtraction(possibility, subset)
                    if not difference:
                        num_naked += 1
                if num_naked == subset_size:
                    for row, col in box_candidates:
                        sudoku_cell = sudoku_matrix[row][col]
                        difference = util.set_subtraction(sudoku_cell.possible_values, subset)
                        if difference:
                            sudoku_cell.possible_values = difference
        for row in range(3):
            for col in range(3):
                check_box(3*row, 3*col)

    def check_rows_hidden(subset_size):
        def check_row(row):
            # print 'row', row
            row_candidates = get_row_candidates(row)
            num_occurrences = get_num_occurrences(row_candidates.values())
            # print 'subset_size', subset_size
            # print row_candidates
            subset = []
            inds = []
            for occurrence in num_occurrences:
                possibility_occurrence = num_occurrences[occurrence]
                if possibility_occurrence > 1 and possibility_occurrence <= subset_size:
                    subset.append(occurrence)
                    inds += occurrence_inds(occurrence, row_candidates)
            inds = list(set(inds))
            if len(subset) == subset_size and len(inds) == subset_size:  # found a hidden subset
                # print 'subset', subset
                # print 'inds ', inds
                for col in row_candidates:
                    sudoku_cell = sudoku_matrix[row][col]
                    difference = util.set_subtraction(sudoku_cell.possible_values, subset)
                    # if len(difference) < len(sudoku_cell.possible_values):
                    if col in inds:
                        # print 'difference', difference
                        # print 'original ', sudoku_cell.possible_values
                        sudoku_cell.possible_values = util.set_subtraction(sudoku_cell.possible_values, difference)
                        # print 'final ', sudoku_cell.possible_values, '\n'
        for row in range(9):
            check_row(row)
    def check_cols_hidden(subset_size):
        def check_col(col):
            col_candidates = get_col_candidates(col)
            num_occurrences = get_num_occurrences(col_candidates.values())
            subset = []
            inds = []
            for occurrence in num_occurrences:
                possibility_occurrence = num_occurrences[occurrence]
                if possibility_occurrence > 1 and possibility_occurrence <= subset_size:
                    subset.append(occurrence)
                    inds += occurrence_inds(occurrence, col_candidates)
            inds = list(set(inds))
            if len(subset) == subset_size and len(inds) == subset_size:  # found a hidden subset
                for row in col_candidates:
                    sudoku_cell = sudoku_matrix[row][col]
                    difference = util.set_subtraction(sudoku_cell.possible_values, subset)
                    # if len(difference) < len(sudoku_cell.possible_values):
                    if row in inds:
                        sudoku_cell.possible_values = util.set_subtraction(sudoku_cell.possible_values, difference)
        for col in range(9):
            check_col(col)
    def check_boxes_hidden(subset_size):
        def check_box(row, col):
            box_candidates = get_box_candidates(row, col)
            num_occurrences = get_num_occurrences(box_candidates.values())
            subset, inds = [], []
            for occurrence in num_occurrences:
                possibility_occurrence = num_occurrences[occurrence]
                if possibility_occurrence > 1 and possibility_occurrence <= subset_size:
                    subset.append(occurrence)
                    inds += occurrence_inds(occurrence, box_candidates)
            inds = list(set(inds))
            if len(subset) == subset_size and len(inds) == subset_size:
                for row, col in box_candidates:
                    sudoku_cell = sudoku_matrix[row][col]
                    difference = util.set_subtraction(sudoku_cell.possible_values, subset)
                    if row in inds:
                        sudoku_cell.possible_values = util.set_subtraction(sudoku_cell.possible_values, difference)
        for row in range(3):
            for col in range(3):
                check_box(3*row, 3*col)

    def naked_subsets():
        for subset_size in range(2, 5):
            check_rows_naked(subset_size)
            check_cols_naked(subset_size)
            check_boxes_naked(subset_size)
    def hidden_subsets():
        for subset_size in range(2, 5):
            check_rows_hidden(subset_size)
            check_cols_hidden(subset_size)
            check_boxes_hidden(subset_size)

    naked_subsets()
    hidden_subsets()
    return sudoku_matrix

def get_naked_single(surrounding_values):
    vs = sorted(surrounding_values)
    if vs[0] != 1:  # 1 is missing
        return 1

    for i in range(8):
        if vs[i] != i + 1:
            return i + 1
    return 9  # nums [1, 8] are in the list

def remove_possibility_from_box(sudoku_matrix, row, col, val):
    """ remove possibility `val` from box associated with row, col """
    row_ind, col_ind = get_init_group_ind(row), get_init_group_ind(col)
    row_ind_range = range(row_ind, row_ind + 3)
    col_ind_range = range(col_ind, col_ind + 3)

    for r in row_ind_range:
        for c in col_ind_range:
            sudoku_cell = sudoku_matrix[r][c]
            if isinstance(sudoku_cell, SudokuPossibilities):
                sudoku_cell.remove_elem(val)

def remove_possibility_from_row(sudoku_matrix, row, val, col=None):
    """ remove possiblity `val` from row `row`
        if col argument is provided, will not affect columns in `col` """
    row_range = range(len(sudoku_matrix))
    if col is not None:
        row_range = [i for i in row_range if i not in col]
    for i in row_range:
        sudoku_cell = sudoku_matrix[row][i]
        if isinstance(sudoku_cell, SudokuPossibilities):
            sudoku_cell.remove_elem(val)

def remove_possibility_from_col(sudoku_matrix, col, val, row=None):
    """  remove possibility `val` from col `col`
         if row argument is provided, will not affect rows in `row` """
    col_range = range(len(sudoku_matrix))
    if row is not None:
        col_range = [i for i in col_range if i not in row]
    for i in col_range:
        sudoku_cell = sudoku_matrix[i][col]
        if isinstance(sudoku_cell, SudokuPossibilities):
            sudoku_cell.remove_elem(val)

def naked_single(sudoku_matrix):
    while True:
        num_possibilities = count_num_possibilities(sudoku_matrix)

        for row in range(len(sudoku_matrix)):
            for col in range(len(sudoku_matrix)):
                sudoku_cell = sudoku_matrix[row][col]
                if isinstance(sudoku_cell, SudokuValue):  # remove this value from all corresponding SudokuPossibilities
                    sudoku_value = sudoku_cell.value
                    remove_possibility_from_box(sudoku_matrix, row, col, sudoku_value)
                    remove_possibility_from_row(sudoku_matrix, row, sudoku_value)
                    remove_possibility_from_col(sudoku_matrix, col, sudoku_value)
                # check if we can eliminate values of cell to a single value
                else:
                    surrounding_values = get_surrounding_values(sudoku_matrix, row, col)
                    if len(surrounding_values) == 8:  # found a naked single
                        naked_single = get_naked_single(surrounding_values)
                        # set sudoku cell to be naked single
                        set_value_in_matrix(sudoku_matrix, row, col, naked_single)
                        # print 'setting (%i,%i) = %i (naked single)' %(row, col, naked_single)
                        # print matrix_to_string(sudoku_matrix)
                    else:  # update possible values
                        sudoku_cell.possible_values = util.set_subtraction(sudoku_cell.possible_values, surrounding_values)

        if num_possibilities == count_num_possibilities(sudoku_matrix):
            break
    return sudoku_matrix

def only_cell_in_row(sudoku_matrix, row, col):
    col_ind_start = get_init_group_ind(col)
    col_to_check = [i for i in range(col_ind_start, col_ind_start + 3) if i != col]
    for c in col_to_check:
        if isinstance(sudoku_matrix[row][c], SudokuPossibilities):
            return False
    return True

def only_cell_in_col(sudoku_matrix, row, col):
    row_ind_start = get_init_group_ind(row)
    row_to_check = [i for i in range(row_ind_start, row_ind_start + 3) if i != row]
    for r in row_to_check:
        if isinstance(sudoku_matrix[r][col], SudokuPossibilities):
            return False
    return True

def check_row_hidden_single(sudoku_matrix, row, col):
    row_ind = get_init_group_ind(row)
    row1, row2 = [i for i in range(row_ind, row_ind + 3) if i != row]

    box_vals = get_box_vals(sudoku_matrix, row, col)
    row1_vs = set(util.set_subtraction(get_row_vals(sudoku_matrix, row1, col), box_vals))
    row2_vs = set(util.set_subtraction(get_row_vals(sudoku_matrix, row2, col), box_vals))
    intersect = list(set.intersection(row1_vs, row2_vs))

    if len(intersect) > 1:
        print matrix_to_string(sudoku_matrix)
        raise Exception('found more than 1 possibility for hidden single')
    elif intersect:
        return intersect[0]
    else:  # no hidden single
        return 0

def check_col_hidden_single(sudoku_matrix, row, col):
    col_ind = get_init_group_ind(col)
    col1, col2 = [i for i in range(col_ind, col_ind + 3) if i != col]

    box_vals = get_box_vals(sudoku_matrix, row, col)
    col1_vs = set(util.set_subtraction(get_col_vals(sudoku_matrix, row, col1), box_vals))
    col2_vs = set(util.set_subtraction(get_col_vals(sudoku_matrix, row, col2), box_vals))
    intersect = list(set.intersection(col1_vs, col2_vs))

    if len(intersect) > 1:
        print row, col
        print intersect
        print matrix_to_string(sudoku_matrix)
        raise Exception('found more than 1 possibility for hidden single')
    elif intersect:
        return intersect[0]
    else:  # no hidden single
        return 0

def hidden_single(sudoku_matrix):
    num_uncertain_cells = count_uncertain_values(sudoku_matrix)
    while True:
        num_uncertain_cells_beginning = num_uncertain_cells

        for row in range(len(sudoku_matrix)):
            for col in range(len(sudoku_matrix)):
                sudoku_cell = sudoku_matrix[row][col]
                if isinstance(sudoku_cell, SudokuValue):  # value already established
                    continue
                # check for hidden single
                if only_cell_in_row(sudoku_matrix, row, col):
                    result = check_row_hidden_single(sudoku_matrix, row, col)
                    if result:
                        set_value_in_matrix(sudoku_matrix, row, col, result)
                        # print 'setting (%i,%i) = %i (hidden_single -- only cell in row)' %(row, col, result)
                        # print matrix_to_string(sudoku_matrix)
                        num_uncertain_cells -= 1
                        continue  # if we can fill the cell, there's no point executing 2nd if because we've already solved the value
                    pass
                if only_cell_in_col(sudoku_matrix, row, col):
                    result = check_col_hidden_single(sudoku_matrix, row, col)
                    if result:
                        set_value_in_matrix(sudoku_matrix, row, col, result)
                        # print 'setting (%i,%i) = %i (hidden_single -- only cell in col)' %(row, col, result)
                        # print matrix_to_string(sudoku_matrix)
                        num_uncertain_cells -= 1
        if num_uncertain_cells == num_uncertain_cells_beginning:
            break
    return sudoku_matrix

if __name__ == '__main__':
    # print matrix_is_valid(convert_matrix(matrix))
    # print matrix_to_string(convert_matrix(matrix))
    sm = sudoku(matrix)
    print matrix_to_string(sm)
