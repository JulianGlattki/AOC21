SCORES_TABLES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

MATCHES_TABLE = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

file1 = open('input.txt', 'r')
lines = [list(line.strip('\n')) for line in file1.readlines()]

score = 0

for line in lines:
    stack = []
    for char in line:
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        elif char in SCORES_TABLES.keys():
            last_item = stack.pop()

            if MATCHES_TABLE[char] != last_item:
                score = score + SCORES_TABLES[char]
                break

print(score)
