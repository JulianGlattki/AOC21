from functools import reduce
RISK_LEVEL_ADD = 1


# start with a low point
# go to each adjacent point
    # check if the adjacent points adjacent points are equal to height of adjacent point + 1
        # if it is true for one go to its adjacent points excluding the the current point
            # remember to save the adjacent points coordinates
        # else return all collected coordinates
def is_low_point(matrix, row, column):
    if matrix[row][column] is None or matrix[row][column] == 9:
        return False
    if row - 1 >= 0 and matrix[row - 1][column] is not None and matrix[row - 1][column] <= matrix[row][column]:
        return False
    if row + 1 < len(matrix) and matrix[row + 1][column] is not None and matrix[row + 1][column] <= matrix[row][column]:
        return False
    if column - 1 >= 0 and matrix[row][column - 1] is not None and matrix[row][column - 1] <= matrix[row][column]:
        return False
    if column + 1 < len(matrix[row]) and matrix[row][column + 1] is not None and matrix[row][column + 1] <= matrix[row][column]:
        return False

    return True


def get_coordinates_of_basin(all_coordinates_of_basin, row, column):
    if matrix[row][column] is not None and (row, column) not in all_coordinates_of_basin and matrix[row][column] != 9:
        all_coordinates_of_basin.add((row, column))
        matrix[row][column] = None
        if row - 1 >= 0 and matrix[row - 1][column] is not None and matrix[row - 1][column] != 9:
            all_coordinates_of_basin.update(get_coordinates_of_basin(all_coordinates_of_basin, row - 1, column))
        if row + 1 < len(matrix) and matrix[row + 1][column] is not None and matrix[row + 1][column] != 9:
            all_coordinates_of_basin.update(get_coordinates_of_basin(all_coordinates_of_basin, row + 1, column))
        if column - 1 >= 0 and matrix[row][column - 1] is not None and matrix[row][column - 1] != 9:
            all_coordinates_of_basin.update(get_coordinates_of_basin(all_coordinates_of_basin, row, column - 1))
        if column + 1 < len(matrix[row]) and matrix[row][column + 1] is not None and matrix[row][column + 1] != 9:
            all_coordinates_of_basin.update(get_coordinates_of_basin(all_coordinates_of_basin, row, column + 1))

    return all_coordinates_of_basin


file1 = open('input.txt', 'r')
matrix = [list(map(int, list(line.strip('\n')))) for line in file1.readlines()]

all_coordinates_of_all_basins = []

for row_index in range(len(matrix)):
    for column_index in range(len(matrix[row_index])):
        coordinates_of_basin = get_coordinates_of_basin(set(), row_index, column_index)
        if len(coordinates_of_basin) != 0:
            all_coordinates_of_all_basins.append(coordinates_of_basin)

three_biggest_basins = [len(basin) for basin in sorted(all_coordinates_of_all_basins, key=len, reverse=True)[:3]]
print(reduce(lambda x, y: x * y, three_biggest_basins))