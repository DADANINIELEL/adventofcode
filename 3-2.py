from readinput import read_input


def get_oxygen_generator_rating(data: list, bit_num=0) -> str:
    if len(data) == 1:
        return data[0]
    data_1 = []
    data_0 = []
    print(data)
    for d in data:
        if d[bit_num] == "1":
            data_1.append(d)
        else:
            data_0.append(d)
    if len(data_0) > len(data_1):
        new_data = data_0
    else:
        new_data = data_1
    return get_oxygen_generator_rating(new_data, bit_num + 1)


def get_CO2_scrubber_rating(data: list, bit_num=0) -> str:
    if len(data) == 1:
        return data[0]
    data_1 = []
    data_0 = []
    for d in data:
        if d[bit_num] == "1":
            data_1.append(d)
        else:
            data_0.append(d)
    if len(data_1) < len(data_0):
        new_data = data_1
    else:
        new_data = data_0
    return get_CO2_scrubber_rating(new_data, bit_num + 1)


diag_data = read_input("3", "1")
lines = len(diag_data)
half = lines / 2
print(lines)

ogr = get_oxygen_generator_rating(diag_data)
co2sr = get_CO2_scrubber_rating(diag_data)

print(f"{ogr} * {co2sr}")
ogr = int(ogr, base=2)
co2sr = int(co2sr, base=2)
print(f"{ogr} * {co2sr} = {ogr*co2sr}")
