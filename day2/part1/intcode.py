instructions = [int(a) for a in input().split(',')]

instructions[1] = 12
instructions[2] = 2

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

print(instructions)
print()
print(instructions[0])
