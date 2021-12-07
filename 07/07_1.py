import statistics

file1 = open('input.txt', 'r')
crabs = list(map(int, file1.readline().strip('\n').split(',')))
median = statistics.median(crabs)
print(int(sum(abs(x - median) for x in crabs)))