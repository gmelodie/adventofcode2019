import sys
import numpy as np
import intcode


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 tractor.py <intcode_file>")
        exit(1)

    instructions = intcode.load_instructions(sys.argv[1])


    output = []
    for i in range(50):
        for j in range(50):
            idx, rboffset = intcode.execute(instructions.copy(), \
                                            inputdata=[i, j])
            output.append(intcode.RETVAL)
            print(intcode.RETVAL, end='')
        print()



    output = np.array(output)
    print(output)
    print(output[output == 1])
    print(len(output[output == 1]))
