from readinput import read_input

input_data = read_input("1", "1")
depth_data = [int(d) for d in input_data]
depth_data_sum = [sum(depth_data[i : i + 3]) for i in range(0, len(depth_data) - 2)]
print(depth_data_sum)
larger = 0
previous_depth_sum = depth_data_sum.pop(0)
for depth_sum in depth_data_sum:
    if depth_sum > previous_depth_sum:
        larger += 1
    previous_depth_sum = depth_sum
print(larger)
