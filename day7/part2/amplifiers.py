import sys
import intcode
from itertools import cycle

combinations = []
LOW_SET = 5
HIGH_SET = 9

def combine(instructions, used):
    if len(used) == 5:
        combinations.append(used)

    for i in range(LOW_SET, HIGH_SET+1):
        if i not in used:
            aux = used.copy()
            aux.append(i)
            combine(instructions.copy(), aux)

def init_amplifiers(combination):
    initval = 0
    instances = [instructions.copy(),
                 instructions.copy(),
                 instructions.copy(),
                 instructions.copy(),
                 instructions.copy()]
    idxs = [0, 0, 0, 0, 0]

    for i, setting in enumerate(combination):
        idxs[i] = intcode.execute(instances[i], idxs[i], \
                                  [setting, initval])
        initval = intcode.RETVAL

    return idxs, instances, initval


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 amplifiers.py <instructions_file>")
        exit(1)

    instructions = intcode.load_instructions(sys.argv[1])
    combine(instructions.copy(), list())

    maxthrust = 0
    for combination in combinations:
        idxs, instances, initval = init_amplifiers(combination)

        for i in cycle(range(5)):
            idxs[i] = intcode.execute(instances[i], idxs[i], \
                                      [initval])
            initval = intcode.RETVAL
            if instances[4][idxs[4]] == 99: # last amplifier halted
                break

        if initval > maxthrust:
            maxthrust = initval
    print("Maxthrust: ", maxthrust)





