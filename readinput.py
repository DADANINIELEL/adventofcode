def read_input(day_number: str = "1", test_number: str = "1") -> list:
    input_data = []
    with open(day_number + "-" + test_number + ".txt", "r") as f:
        for line in f:
            input_data.append(line.strip())
    return input_data


def read_input_boards() -> tuple:
    bingo_numbers = []
    boards = [[]]
    with open("4-1.txt", "r") as f:
        bingo_numbers = f.readline().strip().split(",")
        print(" ".join(bingo_numbers))
        bingo_numbers = [int(b) for b in bingo_numbers]
        f.readline()
        i = 0
        for line in f:
            if line == "\n":
                i += 1
                boards.append([])
            else:
                data_line = [int(d) for d in line.split()]
                boards[i].append(data_line)

    print(f"Boards: {len(boards)}")
    for board in boards:
        x = len(board)
        y = int(sum([len(yn) for yn in board]) / 5)
        print(f"{x}x{y} ", end="")
    return (bingo_numbers, boards)
