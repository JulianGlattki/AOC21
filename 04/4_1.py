MARKER = -1


def check_lists_for_bingo(lists_to_check):
    for list_to_check in lists_to_check:
        if list_to_check.count(MARKER) == len(list_to_check):
            return True


def mark_number_on_board(number, board):
    return [[MARKER if col == number else col for col in row] for row in board]


file1 = open('input.txt', 'r')
numbers_drawn = file1.readline().strip('\n').split(',')
numbers_drawn = list(map(int, numbers_drawn))
file1.readline()

boards = []
current = []
for line in file1:
    if line[:-1]:
        current.append(list(map(int, line.split())))
        if len(current) == 5:
            boards.append(current)
            current = []

winner_boards_and_numbers = []
for number in numbers_drawn:
    for index, board in enumerate(boards):
        board = mark_number_on_board(number, board)
        boards[index] = board
        if check_lists_for_bingo(board) or check_lists_for_bingo(list(zip(*board))):
            print('BINGO')
            print('Number drawn: ' + str(number))
            print('Winning board: ' + str(board))
            print('Unmarked * Number: ' + str(
                sum(sum([n for n in x if n != -1]) for x in board) * number))
            exit()



