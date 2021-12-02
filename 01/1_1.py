file1 = open('input.txt', 'r')
lines = [int(line.strip('\n')) for line in file1.readlines()]

current_max = int(lines[0])
increased = 0

for line in lines[1:]:
    if line > current_max:
        increased += 1
    current_max = line

print(increased)
    
