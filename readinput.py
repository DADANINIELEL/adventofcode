def read_input(day_number: str = "1", test_number: str = "1") -> list:
    input_data = []
    with open(day_number + "-" + test_number + ".txt", "r") as f:
        for line in f:
            input_data.append(line.strip())
    return input_data
