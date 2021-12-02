file1 = open('input.txt', 'r')
lines = [line.strip('\n').split(" ") for line in file1.readlines()]


horizontal = 0
depth = 0
aim = 0

for line in lines:
    direction = line[0] 
    distance = int(line[1])

    if direction == 'forward':
        horizontal += distance
        depth += aim * distance
    elif direction == 'up':
       aim -= distance
    else:
       aim += distance

print(depth * horizontal)
