instructions = [int(a) for a in input().split(',')]

instructions[1] = 12
instructions[2] = 2

idx = 0

opcode = instructions[idx]
while opcode != 99:
    print("Idx == ", idx)
    if opcode == 1:
        instructions[idx+3] = instructions[idx+1] + instructions[idx+2]
    elif opcode == 2:
        instructions[idx+3] = instructions[idx+1] * instructions[idx+2]
    else:
        print("Unexpected opcode ", opcode)
        print(instructions)
        exit(1)

    idx += 4
    opcode = instructions[idx]

print(instructions)
print()
print(instructions[0])
