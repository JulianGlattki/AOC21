RISK_LEVEL_ADD = 1


def is_low_point(matrix, row, column):
    if row - 1 >= 0 and matrix[row - 1][column] <= matrix[row][column]:
        return False
    if row + 1 < len(matrix) and matrix[row + 1][column] <= matrix[row][column]:
        return False
    if column - 1 >= 0 and matrix[row][column - 1] <= matrix[row][column]:
        return False
    if column + 1 < len(matrix[row]) and matrix[row][column + 1] <= matrix[row][column]:
        return False

    return True


file1 = open('input.txt', 'r')
matrix = [list(map(int, list(line.strip('\n')))) for line in file1.readlines()]


all_risk_levels = 0

for row_index in range(len(matrix)):
    for column_index in range(len(matrix[row_index])):
        if is_low_point(matrix, row_index, column_index):
            all_risk_levels = all_risk_levels + RISK_LEVEL_ADD + matrix[row_index][column_index]


print(all_risk_levels)