

def exec_strip(instructions):
    idx = 0

    opcode = instructions[idx]
    while opcode != 99:

        a = instructions[idx+1]
        b = instructions[idx+2]
        i = instructions[idx+3]

        if opcode == 1:
            instructions[i] = instructions[a] + instructions[b]
        elif opcode == 2:
            instructions[i] = instructions[a] * instructions[b]
        else:
            print("Unexpected opcode ", opcode)
            print(instructions)
            exit(1)

        idx += 4
        opcode = instructions[idx]

    return instructions


if __name__ == '__main__':

    instructions = [int(a) for a in input().split(',')]

    expected = 19690720

    # Brute force for combination of values that produce 19690720
    for i in range(100):
        for j in range(100):
            instructions[1] = i
            instructions[2] = j
            endStrip = exec_strip(instructions.copy())
            if endStrip[0] == expected:
                print("noun == ", endStrip[1])
                print("verb == ", endStrip[2])
                answer = 100*endStrip[1] + endStrip[2]
                print("100 * noun + verb == ", answer)
                exit(0)

    print("Couldn't find correct values")
    exit(1)











