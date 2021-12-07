file1 = open('input.txt', 'r')
crabs = list(map(int, file1.readline().strip('\n').split(',')))
best = None

for i in range(min(crabs), max(crabs)):
    fuel_spent = sum((sum(y for y in (range(1, abs(x - i) + 1))) for x in crabs))
    print(fuel_spent)

    if best is None or fuel_spent < best:
        best = fuel_spent

print(int(best))



