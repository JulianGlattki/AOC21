file1 = open('input.txt', 'r')
all_lines_split = [line.strip('\n').split('|') for line in file1.readlines()]
# signals = [line[0].rstrip(' ').split(' ') for line in all_lines_split]

output_values = [line[1].lstrip(' ').split(' ') for line in all_lines_split]

count = 0
for output_value in output_values:
    for value in output_value:
        if len(value) in [2, 3, 4, 7]:
            count = count + 1

print(count)