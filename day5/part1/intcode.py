def get_modes(instructions, idx):
    params = []
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
    if opcode == 1 or opcode == 2:
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

    return params


def interpret(instructions, idx):
    opcode, modes = get_modes(instructions, idx)
    params = get_params(instructions, idx, opcode, modes)

    print("Raw instruction:", instructions[idx])
    print("Idx:", idx)
    print("Opcode:", opcode)
    print("Params:", params)
    print("Modes:", modes)

    if opcode == 1:
        print("Sum: ", instructions[params[0]], "+", instructions[params[1]])
        instructions[params[2]] = instructions[params[0]] + instructions[params[1]]
        return idx+4

    elif opcode == 2:
        print("Mult: ", instructions[params[0]], "*", instructions[params[1]])
        instructions[params[2]] = instructions[params[0]] * instructions[params[1]]
        return idx+4

    elif opcode == 3:
        instructions[params[0]] = int(input())
        return idx+2

    elif opcode == 4:
        print("Opcode 4: ", instructions[params[0]])
        return idx+2

    elif opcode == 99:
        return -1

    else:
        print("Unexpected opcode ", opcode)
        print(instructions)
        exit(1)



if __name__ == "__main__":

    with open("intcode_input.txt") as fp:
        for line in fp:
            instructions = [int(a) for a in line.strip().split(',')]

    idx = 0

    while idx != -1:
        idx = interpret(instructions, idx)

    print("FINISHED")
    # print(instructions)
