import sys

DEBUG = False # debugging flag
RETVAL = None # return value: last output instruction
RBOFFSET = 0 # offset to be used in relative base mode

operation_types = {
    1: {
        'name': 'sum',
        'nparams': 3,
        'opcode': 1,
    },
    2: {
        'name': 'mult',
        'nparams': 3,
        'opcode': 2,
    },
    3: {
        'name': 'input',
        'nparams': 1,
        'opcode': 3,
    },
    4: {
        'name': 'output',
        'nparams': 1,
        'opcode': 4,
    },
    5: {
        'name': 'jump-if-true',
        'nparams': 2,
        'opcode': 5,
    },
    6: {
        'name': 'jump-if-false',
        'nparams': 2,
        'opcode': 6,
    },
    7: {
        'name': 'less than',
        'nparams': 3,
        'opcode': 7,
    },
    8: {
        'name': 'equals',
        'nparams': 3,
        'opcode': 8,
    },
    9: {
        'name': 'ajdust rb offset',
        'nparams': 1,
        'opcode': 9,
    },
    99: {
        'name': 'halt',
        'nparams': 0,
        'opcode': 99,
    },
}

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
    for i in range(operation_types[opcode]['nparams']):
        if modes[i] == 0:
            params.append(instructions[idx+i+1])
        elif modes[i] == 1:
            params.append(idx+i+1)
        elif modes[i] == 2:
            params.append(instructions[idx+i+1]+RBOFFSET)

    return params


def _interpret(instructions, idx, inputdata):
    opcode, modes = _get_modes(instructions, idx)
    params = _get_params(instructions, idx, opcode, modes)

    if DEBUG:
        print('===============')
        print("Operation type:", operation_types[opcode])
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

    elif opcode == 9: # adjust relative base offset
        global RBOFFSET
        RBOFFSET += instructions[params[0]]
        if DEBUG:
            print('RBOFFSET:', RBOFFSET)
        return idx+2

    elif opcode == 99:
        return idx

    else:
        print("Unexpected opcode ", opcode)
        print(instructions)
        exit(1)


def execute(instructions, startidx=0, inputdata=None):
    idx = -1
    new_idx = startidx
    while new_idx != idx:
        idx = new_idx
        new_idx = _interpret(instructions, idx, inputdata)
    if DEBUG:
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
    # add more memory to instructions queue
    instructions += [0]*1000

    if len(sys.argv) == 3:
        data = []
        with open(sys.argv[2]) as inputfile:
            for line in fp:
                data.append(int(line.strip()))
        execute(instructions, inputdata=data)
    else:
        execute(instructions)














