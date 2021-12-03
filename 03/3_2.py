def filter_list(list_to_filter, number, index):
    return list(filter(lambda l: l[index] == number, list_to_filter))


def count_zeros_and_ones_in_column(list_to_search, index):
    inverted = list(zip(*list_to_search))[index]
    return inverted.count(0), inverted.count(1)


file1 = open('input.txt', 'r')
lines_split = [list(map(int, list(line.strip('\n')))) for line in file1.readlines()]

MAX_LENGTH = len(lines_split[0])

oxygen_rating_list = lines_split.copy()
scrubber_rating_list = lines_split.copy()

for i in range(MAX_LENGTH):
    if len(oxygen_rating_list) > 1:
        count_zeros, count_ones = count_zeros_and_ones_in_column(oxygen_rating_list, i)
        oxygen_rating_list = filter_list(oxygen_rating_list, 1, i) if count_ones >= count_zeros \
            else filter_list(oxygen_rating_list, 0, i)
    if len(scrubber_rating_list) > 1:
        count_zeros, count_ones = count_zeros_and_ones_in_column(scrubber_rating_list, i)
        scrubber_rating_list = filter_list(scrubber_rating_list, 0, i) if count_ones >= count_zeros \
            else filter_list(scrubber_rating_list, 1, i)

oxygen_rating = int(''.join(map(str, oxygen_rating_list[0])), base=2)
co2_scrubber_rating = int(''.join(map(str, scrubber_rating_list[0])), base=2)

print(oxygen_rating)
print(co2_scrubber_rating)
print(oxygen_rating * co2_scrubber_rating)





    










