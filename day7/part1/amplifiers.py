import sys
import intcode

combinations = []

def combine(instructions, used):
    if len(used) == 5:
        combinations.append(used)
        print(used)

    for i in range(5):
        if i not in used:
            aux = used.copy()
            aux.append(i)
            combine(instructions.copy(), aux)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 amplifiers.py <instructions_file>")
        exit(1)

    instructions = intcode.load_instructions(sys.argv[1])
    combine(instructions.copy(), list())

    maxthrust = 0
    for combination in combinations:
        initval = 0
        for setting in combination:
            initval = intcode.execute(instructions.copy(), [setting, initval])
        if initval > maxthrust:
            maxthrust = initval
    print("Maxthrust: ", maxthrust)





