import itertools
file1 = open('input.txt', 'r')

dots = []
instructions = []
max_x = 0
max_y = 0
for line in file1.readlines():
    if ',' in line:
        pair = [int(e) for e in line.strip('\n').split(',')]
        pair.reverse()
        if pair[0] > max_x:
            max_x = pair[0]
        if pair[1] > max_y:
            max_y = pair[1]
        dots.append(pair)
    elif 'fold' in line:
        instructions.append(line.strip('\n').split(' ')[2])

matrix = [[True if [row, column] in dots else False for column in range(max_y + 1)] for row in range(max_x + 1)]


for instruction in instructions:
    instruction_split = instruction.split('=')
    fold_loc = int(instruction_split[1])
    if instruction_split[0] == 'y':
        upper_half = matrix[:fold_loc]
        lower_half = matrix[fold_loc + 1:]

        for i in range(len(lower_half)):
            new_list = [a or b for a, b
                        in itertools.zip_longest(upper_half[len(upper_half) - 1 - i], lower_half[i], fillvalue=False)]
            upper_half[len(upper_half) - 1 - i] = new_list

        matrix = upper_half
    else:
        left_half = []
        right_half = []
        for i in range(len(matrix)):
            left_half.append([])
            right_half.append([])
            for j in range(len(matrix[i])):

                if j < fold_loc:
                    left_half[i].append(matrix[i][j])
                elif j > fold_loc:
                    right_half[i].append(matrix[i][j])

            left_half[i].reverse()

        for i in range(len(right_half)):
            new_list = [a or b for a, b
                        in itertools.zip_longest(left_half[i], right_half[i], fillvalue=False)]
            right_half[i] = new_list
            right_half[i].reverse()

        print(right_half[0])
        matrix = [t[0] for t in zip(right_half)]


for line in matrix:
    l = ''
    for column in line:
        l += 'T' if column else '.'
    print(l)

count = 0
for line in matrix:
    for column in line:
        if column:
            count = count + 1

print(count)






