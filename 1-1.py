from readinput import read_input

input_data = read_input("1", "1")
depth_data = [int(d) for d in input_data]
print(depth_data)
larger = 0
previous_depth = depth_data.pop(0)
for depth in depth_data:
    if depth > previous_depth:
        larger += 1
    previous_depth = depth
print(larger)
