import sys

def get_modes(instructions, idx):
    instruction = instructions[idx]

    mode3 = instruction // 10000
    instruction -= 10000*mode3

    mode2 = instruction // 1000
    instruction -= 1000*mode2

    mode1 = instruction // 100
    instruction -= 100*mode1

    opcode = instruction

    return opcode, [mode1, mode2, mode3]


def get_params(instructions, idx, opcode, modes):
    params = []
    if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
        if modes[0] == 0:
            params.append(instructions[idx+1])
        else:
            params.append(idx+1)
        if modes[1] == 0:
            params.append(instructions[idx+2])
        else:
            params.append(idx+2)
        if modes[2] == 0:
            params.append(instructions[idx+3])
        else:
            params.append(idx+3)

    elif opcode == 3 or opcode == 4:
        if modes[0] == 0:
            params.append(instructions[idx+1])
        else:
            params.append(idx+1)

    elif opcode == 5 or opcode == 6:
        if modes[0] == 0:
            params.append(instructions[idx+1])
        else:
            params.append(idx+1)
        if modes[1] == 0:
            params.append(instructions[idx+2])
        else:
            params.append(idx+2)

    return params


def interpret(instructions, idx, debug=False):
    opcode, modes = get_modes(instructions, idx)
    params = get_params(instructions, idx, opcode, modes)

    if debug:
        print("Raw instruction:", instructions[idx])
        print("Idx:", idx)
        print("Opcode:", opcode)
        print("Params:", params)
        print("Modes:", modes)

    if opcode == 1: # sum
        instructions[params[2]] = instructions[params[0]] + instructions[params[1]]
        return idx+4

    elif opcode == 2: # mult
        instructions[params[2]] = instructions[params[0]] * instructions[params[1]]
        return idx+4

    elif opcode == 3: # input
        instructions[params[0]] = int(input("INPUT > "))
        return idx+2

    elif opcode == 4: # output
        print("OUTPUT:", instructions[params[0]])
        return idx+2

    elif opcode == 5: # jump-if-true
        if instructions[params[0]] != 0:
            return instructions[params[1]]
        return idx+3

    elif opcode == 6: # jump-if-false
        if instructions[params[0]] == 0:
            return instructions[params[1]]
        return idx+3

    elif opcode == 7: # less than
        if instructions[params[0]] < instructions[params[1]]:
            instructions[params[2]] = 1
        else:
            instructions[params[2]] = 0
        return idx+4

    elif opcode == 8: # equals
        if instructions[params[0]] == instructions[params[1]]:
            instructions[params[2]] = 1
        else:
            instructions[params[2]] = 0
        return idx+4

    elif opcode == 99:
        return -1

    else:
        print("Unexpected opcode ", opcode)
        print(instructions)
        exit(1)



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 intcode.py <input_file>")
        exit(1)

    with open(sys.argv[1]) as fp:
        for line in fp:
            instructions = [int(a) for a in line.strip().split(',')]

    idx = 0

    while idx != -1:
        idx = interpret(instructions, idx)

    print("FINISHED")
    # print(instructions)
