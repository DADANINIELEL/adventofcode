from readinput import read_input

diag_data = read_input("3", "1")
lines = len(diag_data)
half = lines / 2
print(lines)
diag_bits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
gamma_rate = ""
epsilon_rate = ""
for diag_line in diag_data:
    for i, bit in enumerate(diag_line):
        diag_bits[i] += int(bit)
print(diag_bits)
for bit in diag_bits:
    if bit > half:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"
print(int(gamma_rate, base=2) * int(epsilon_rate, base=2))
