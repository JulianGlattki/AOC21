file1 = open('input.txt', 'r')
lanternfish_pop = list(map(int, file1.readline().strip('\n').split(',')))

for i in range(80):
    new_laternfish = []
    for j in range(len(lanternfish_pop)):
        lanternfish_pop[j] = lanternfish_pop[j] - 1

        if lanternfish_pop[j] == -1:
            lanternfish_pop[j] = 6
            new_laternfish.append(8)

    lanternfish_pop += new_laternfish

print(len(lanternfish_pop))


