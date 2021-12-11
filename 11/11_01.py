def is_in_bounds(row, column):
    if 0 <= row < len(matrix):
        if 0 <= column < len(matrix[row]):
            return True
    return False


def inc_and_mark(row, column):
    matrix[row][column] = matrix[row][column] + 1
    if matrix[row][column] > 9:
        matrix[row][column] = 0
        return True
    return False


def flash(row, column):
    global FLASH_COUNT
    FLASH_COUNT = FLASH_COUNT + 1

    if is_in_bounds(row + 1, column) and 1 <= matrix[row + 1][column] < 10:
        if inc_and_mark(row + 1, column):
            flash(row + 1, column)
    if is_in_bounds(row - 1, column) and 1 <= matrix[row - 1][column] < 10:
        if inc_and_mark(row - 1, column):
            flash(row - 1, column)
    if is_in_bounds(row, column + 1) and 1 <= matrix[row][column + 1] < 10:
        if inc_and_mark(row, column + 1):
            flash(row, column + 1)
    if is_in_bounds(row, column - 1) and 1 <= matrix[row][column - 1] < 10:
        if inc_and_mark(row, column - 1):
            flash(row, column - 1)
    if is_in_bounds(row + 1, column + 1) and 1 <= matrix[row + 1][column + 1] < 10:
        if inc_and_mark(row + 1, column + 1):
            flash(row + 1, column + 1)
    if is_in_bounds(row - 1, column + 1) and 1 <= matrix[row - 1][column + 1] < 10:
        if inc_and_mark(row - 1, column + 1):
            flash(row - 1, column + 1)
    if is_in_bounds(row + 1, column - 1) and 1 <= matrix[row + 1][column - 1] < 10:
        if inc_and_mark(row + 1, column - 1):
            flash(row + 1, column - 1)
    if is_in_bounds(row - 1, column - 1) and 1 <= matrix[row - 1][column - 1] < 10:
        if inc_and_mark(row - 1, column - 1):
            flash(row - 1, column - 1)


FLASH_COUNT = 0
file1 = open('input.txt', 'r')
matrix = [list(map(int, list(line.strip('\n')))) for line in file1.readlines()]

for step in range(100):
    matrix = [[column + 1 for column in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 9:
                matrix[i][j] = 0
                flash(i, j)

print(FLASH_COUNT)
