import sys
import numpy as np
import intcode


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 carepack.py <instructions_file>")
        exit(1)

    instructions = intcode.load_instructions(sys.argv[1])
    idx, rboffset = intcode.execute(instructions)
    output = intcode.OUTPUT

    game_map = np.zeros((1000,1000))

    i = 0
    while i < len(output):
        game_map[output[i]][output[i+1]] = output[i+2]
        i += 3

    print(len(game_map[game_map == 2]))


