file1 = open('input.txt', 'r')
lanternfish_pop = list(map(int, file1.readline().strip('\n').split(',')))

pop_count = {}
for fish in lanternfish_pop:
    if pop_count.get(fish) is None:
        pop_count[fish] = 0
    pop_count[fish] += 1


for i in range(256):
    new_pop_count = {}
    for fish, count in pop_count.items():
        if fish == 0:
            new_pop_count[6] = new_pop_count[6] + count if new_pop_count.get(6) is not None else count
            new_pop_count[8] = new_pop_count[8] + count if new_pop_count.get(8) is not None else count
        else:
            new_pop_count[fish - 1] = new_pop_count[fish - 1] + count if new_pop_count.get(fish - 1) is not None else count

    pop_count = new_pop_count

print((sum(pop_count.values())))


