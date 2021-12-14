from readinput import read_input_boards


def board_mark_number(board: list, bingo_number: int) -> int:
    for l, line in enumerate(board):
        for c, col in enumerate(line):
            if col == bingo_number:
                board[l][c] = -1
    for line in board:
        if sum(line) == -5:
            result = sum([c for l in board for c in l if c > 0]) * bingo_number
            for l, line in enumerate(board):
                for c, col in enumerate(line):
                    board[l][c] = -1000
            return result
    for i in range(5):
        if sum([b[i] for b in board]) == -5:
            result = sum([c for l in board for c in l if c > 0]) * bingo_number
            for l, line in enumerate(board):
                for c, col in enumerate(line):
                    board[l][c] = -1000
            return result
    return 0


bingo_numbers, boards = read_input_boards()

for bingo_number in bingo_numbers:
    for board in boards:
        result = board_mark_number(board, bingo_number)
        print(result, end=" ")
        if result:
            print(f"\nbingo score: {result}")
