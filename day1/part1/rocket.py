import fileinput


total_fuel = 0

for line in fileinput.input():
    modmass = int(line)
    total_fuel += int(modmass/3) - 2

print(total_fuel)
