file1 = open('input.txt', 'r')
all_start_end_vectors = [[[int(numb.strip()) for numb in vector.split(',')]
                          for vector in line.strip('\n').split('->')]
                         for line in file1.readlines()]

visited_numbers = {}
for vector_combo in all_start_end_vectors:
    if vector_combo[0][0] == vector_combo[1][0]:
        minmax = (min(vector_combo[0][1], vector_combo[1][1]), max(vector_combo[0][1], vector_combo[1][1]) + 1)
        for y in range(*minmax):
            key = (vector_combo[0][0], y)
            if visited_numbers.get(key) is not None:
                visited_numbers[key] = visited_numbers[key] + 1
            else:
                visited_numbers[key] = 1
    elif vector_combo[0][1] == vector_combo[1][1]:
        minmax = (min(vector_combo[0][0], vector_combo[1][0]), max(vector_combo[0][0], vector_combo[1][0]) + 1)
        for x in range(*minmax):
            key = (x, vector_combo[0][1])
            if visited_numbers.get(key) is not None:
                visited_numbers[key] = visited_numbers[key] + 1
            else:
                visited_numbers[key] = 1
    else:
        x2_adjustment = 1 if vector_combo[0][0] < vector_combo[1][0] else -1
        y2_adjustment = -1 if vector_combo[0][1] > vector_combo[1][1] else 1

        for x, y in zip(range(vector_combo[0][0], vector_combo[1][0] + x2_adjustment, x2_adjustment),
                        range(vector_combo[0][1], vector_combo[1][1] + y2_adjustment, y2_adjustment)):
            key = (x, y)
            if visited_numbers.get(key) is not None:
                visited_numbers[key] = visited_numbers[key] + 1
            else:
                visited_numbers[key] = 1


print(len([times for times in visited_numbers.values() if times > 1]))
