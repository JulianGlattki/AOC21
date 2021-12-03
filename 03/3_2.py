file1 = open('input.txt', 'r')
lines_split = [list(map(int, list(line.strip('\n')))) for line in file1.readlines()]

MAX_LENGTH = len(lines_split[0])

oxygen_rating_list = lines_split.copy()
[oxygen_rating_list := list(filter(lambda l: l[i] == 1, oxygen_rating_list))
    if max(sorted(list(zip(*oxygen_rating_list))[i], reverse=True), key=list(zip(*oxygen_rating_list))[i].count) == 1
    else list(filter(lambda l: l[i] == 0, oxygen_rating_list)) for i in range(MAX_LENGTH)]

scrubber_rating_list = lines_split.copy()
[scrubber_rating_list := list(filter(lambda l: l[i] == 1, scrubber_rating_list))
    if min(sorted(list(zip(*scrubber_rating_list))[i]), key=list(zip(*scrubber_rating_list))[i].count) == 1
    else list(filter(lambda l: l[i] == 0, scrubber_rating_list)) for i in range(MAX_LENGTH)]

print(int(''.join(map(str, oxygen_rating_list[0])), base=2) * int(''.join(map(str, scrubber_rating_list[0])), base=2))