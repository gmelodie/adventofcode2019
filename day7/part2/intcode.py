import sys

RETVAL = None # return value: last output instruction

def _get_modes(instructions, idx):
    instruction = instructions[idx]

    mode3 = instruction // 10000
    instruction -= 10000*mode3

    mode2 = instruction // 1000
    instruction -= 1000*mode2

    mode1 = instruction // 100
    instruction -= 100*mode1

    opcode = instruction

    return opcode, [mode1, mode2, mode3]


def _get_params(instructions, idx, opcode, modes):
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


def _interpret(instructions, idx, inputdata, debug=False):
    opcode, modes = _get_modes(instructions, idx)
    params = _get_params(instructions, idx, opcode, modes)

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
        if inputdata is not None:
            if len(inputdata) == 0:
                return idx # stop execution
            else:
                instructions[params[0]] = inputdata.pop(0)
        else:
            instructions[params[0]] = int(input("INPUT > "))
        return idx+2

    elif opcode == 4: # output
        print("OUTPUT:", instructions[params[0]])
        global RETVAL
        RETVAL = instructions[params[0]] # set return value
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
        return idx

    else:
        print("Unexpected opcode ", opcode)
        print(instructions)
        exit(1)


def execute(instructions, startidx=0, inputdata=None, debug=False):
    idx = -1
    new_idx = startidx
    while new_idx != idx:
        idx = new_idx
        new_idx = _interpret(instructions, idx, inputdata)
    if debug:
        print("FINISHED")
    return idx


def load_instructions(filename):
    with open(sys.argv[1]) as fp:
        for line in fp:
            instructions = [int(a) for a in line.strip().split(',')]

    return instructions


if __name__ == "__main__":
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("usage: python3 intcode.py <instructions_file> [input_file]")
        exit(1)

    instructions = load_instructions(sys.argv[1])

    if len(sys.argv) == 3:
        data = []
        with open(sys.argv[2]) as inputfile:
            for line in fp:
                data.append(int(line.strip()))
        execute(instructions, inputdata=data)
    else:
        execute(instructions)














