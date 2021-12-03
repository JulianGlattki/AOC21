file1 = open('input.txt', 'r')

most_common_bit_per_column = [str(max(column, key=column.count)) for column in zip(*[map(int, list(line.strip('\n'))) for line in file1.readlines()])]

most_common_bits_as_string = ''.join(most_common_bit_per_column)

gamma_rate = int(most_common_bits_as_string, base=2)
epsilon_rate = int(most_common_bits_as_string.translate({48: 49, 49:48}), base=2)

print(gamma_rate * epsilon_rate)




