from functools import reduce

SCORES_TABLES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

MATCHES_TABLE = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

MATCHES_TABLE_INVERTED = {v: k for k, v in MATCHES_TABLE.items()}

file1 = open('input.txt', 'r')
lines = [list(line.strip('\n')) for line in file1.readlines()]


incomplete_lines = []

score = []
for line in lines:
    stack = []
    corrupted = False
    for char in line:
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        elif char in SCORES_TABLES.keys():
            last_item = stack.pop()
            if MATCHES_TABLE[char] != last_item:
                corrupted = True
                break

    if not corrupted:
        reversed_stack = reversed(stack)
        curr_score = reduce(lambda a, b: a * 5 + SCORES_TABLES[MATCHES_TABLE_INVERTED[b]], reversed_stack, 0)
        score.append(curr_score)

score.sort()
print(score[int(len(score) / 2)])

