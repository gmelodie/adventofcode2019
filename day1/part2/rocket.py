import fileinput


total_fuel = 0

for line in fileinput.input():
    modmass = int(line)
    modfuel = int(modmass/3) - 2

    fuelfuel = int(modfuel/3) - 2
    while fuelfuel > 0:
        modfuel += fuelfuel
        fuelfuel = int(fuelfuel/3) - 2

    print(modmass, " => ", modfuel)
    total_fuel += modfuel

print(total_fuel)
