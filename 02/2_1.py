file1 = open('input.txt', 'r')
lines = [line.strip('\n').split(" ") for line in file1.readlines()]


horizontal = 0
depth = 0

for line in lines:
    direction = line[0] 
    distance = int(line[1])
    if direction == 'forward':
        horizontal += distance
    elif direction == 'up':
       depth -= distance
    else:
       depth += distance

print(depth * horizontal)
