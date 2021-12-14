from readinput import read_input

pos_data = read_input("2", "1")
pos_data_forward = 0
pos_data_depth = 0
pos_aim = 0
# print(depth_data_sum)
# previous_depth_sum = depth_data_sum.pop(0)
for pos in pos_data:
    direction, data = pos.split()
    data = int(data)
    if direction == "forward":
        pos_data_forward += data
        pos_data_depth += data * pos_aim
    elif direction == "up":
        pos_aim -= data
    elif direction == "down":
        pos_aim += data
    else:
        print("Error texto")
print(pos_data_forward)
print(pos_data_depth)
print(pos_data_forward * pos_data_depth)
