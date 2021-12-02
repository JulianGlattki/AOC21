from functools import reduce

SLIDING_WINDOW_SIZE = 3

file1 = open('input.txt', 'r')
lines = [int(line.strip('\n')) for line in file1.readlines()]

current_max = sum(lines[0:SLIDING_WINDOW_SIZE]) if len(lines) >= SLIDING_WINDOW_SIZE else None
counter = 0

for i in range(1, (len(lines)-SLIDING_WINDOW_SIZE + 1)):
    if sum(lines[i:i+SLIDING_WINDOW_SIZE]) > current_max:
        counter += 1
    current_max = sum(lines[i:i+SLIDING_WINDOW_SIZE])

print(counter)
