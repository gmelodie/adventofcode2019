import sys
import numpy as np
import intcode


def bin_search(instructions):
    low = 0
    high = 1000

    for y in range(120, 1000):
        while low < high:
            mid = (low+high)//2
            idx, rboffset = intcode.execute(instructions.copy(), \
                                            inputdata=[i, j])
            output.append(intcode.RETVAL)

    return -1, -1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 tractor.py <intcode_file>")
        exit(1)

    instructions = intcode.load_instructions(sys.argv[1])

    # x, y = bin_search(instructions)

    y = x = 1000
    while True:
        print(x, y)
        idx, rboffset = intcode.execute(instructions.copy(), \
                                        inputdata=[x, y])
        if intcode.RETVAL == 0:
            x += 1
            continue

        idx, rboffset = intcode.execute(instructions.copy(), \
                                        inputdata=[x+99, y])
        if intcode.RETVAL == 0:
            y += 1
            continue

        idx, rboffset = intcode.execute(instructions.copy(), \
                                        inputdata=[x, y+99])
        if intcode.RETVAL == 0:
            x += 1
            continue
        else:
            break



    print(x*10000 + y)
