def decode(segments):
    one = next(filter(lambda x: len(x) == 2, segments))
    four = next(filter(lambda x: len(x) == 4, segments))
    seven = next(filter(lambda x: len(x) == 3, segments))
    eight = next(filter(lambda x: len(x) == 7, segments))
    two_three_five = [set(list(x)) for x in set(list(filter(lambda x: len(x) == 5, segments)))]
    zero_six_nine = [set(list(x)) for x in set(list(filter(lambda x: len(x) == 6, segments)))]

    top_left_and_bottom_left = set.union(*two_three_five) - set.intersection(*two_three_five) \
                               - set.intersection(list(two_three_five)[0], list(two_three_five)[1]) \
                               - set.intersection(list(two_three_five)[0], list(two_three_five)[2]) \
                               - set.intersection(list(two_three_five)[1], list(two_three_five)[2])

    top_left = [x for x in top_left_and_bottom_left if x in four][0]
    bottom_left = [x for x in top_left_and_bottom_left if x not in four][0]
    middle = list(set(one) ^ set(four) ^ set(top_left))[0]

    zero = [x for x in zero_six_nine if middle not in x][0]
    two = [x for x in two_three_five if bottom_left in x][0]
    five = [x for x in two_three_five if top_left in x][0]
    three = [x for x in two_three_five if not bottom_left in x and not top_left in x][0]
    six = [x for x in zero_six_nine if bottom_left in x and x != zero][0]
    nine = [x for x in zero_six_nine if not bottom_left in x and x != zero][0]

    return {
        str(''.join(sorted(zero))): 0,
        str(one): 1,
        str(''.join(sorted(two))): 2,
        str(''.join(sorted(three))): 3,
        str(''.join(sorted(four))): 4,
        str(''.join(sorted(five))): 5,
        str(''.join(sorted(six))): 6,
        str(seven): 7,
        str(eight): 8,
        str(''.join(sorted(nine))): 9
    }


file1 = open('input.txt', 'r')
all_lines_split = [line.strip('\n').split('|') for line in file1.readlines()]

signals = [[''.join(sorted(segment)) for segment in line[0].rstrip(' ').split(' ')] for line in all_lines_split]
output_values = [[''.join(sorted(segment)) for segment in line[1].lstrip(' ').split(' ')] for line in all_lines_split]

all_output_values = 0

for signal, output in zip(signals, output_values):
    decoded = decode(signal)

    output_nr = ''
    for o in output:
        output_nr += str(decoded[str(o)])

    all_output_values = all_output_values + int(output_nr)

print(all_output_values)
