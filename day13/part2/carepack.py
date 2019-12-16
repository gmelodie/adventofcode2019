import sys
import numpy as np
import intcode

MAX_SCORE = 0

def build_game_map(output):
    game_data = {0: [], 1: [], 2: [], 3: (), 4: ()}
    game_map = np.zeros((100,100))
    i = 0
    while i < len(output):
        if output[i] == -1 and output[i+1] == 0: # show score
            score = output[i+2]
            # print("Score:", score)
            global MAX_SCORE
            if score > MAX_SCORE:
                MAX_SCORE = score
        else:
            game_map[output[i+0]][output[i+1]] = output[i+2]
            if output[i+2] == 3 or output[i+2] == 4:
                game_data[output[i+2]] = (output[i+0], output[i+1])
            else:
                game_data[output[i+2]].append((output[i+0], \
                                              output[i+1]))
        i += 3

    return game_data, game_map


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 carepack.py <instructions_file>")
        exit(1)

    instructions = intcode.load_instructions(sys.argv[1])
    instructions[0] = 2  # put 'quarters'
    idx, rboffset = intcode.execute(instructions, inputdata=[])
    output = intcode.OUTPUT
    game_data, game_map = build_game_map(output)

    while len(game_map[game_map == 2]) > 0:
        move = (game_data[4][0] > game_data[3][0]) - (game_data[4][0] < game_data[3][0])

        idx, rboffset = intcode.execute(instructions, \
                                        startidx=idx, \
                                        rboffset=rboffset,\
                                        inputdata=[move])
        output = intcode.OUTPUT
        game_data, game_map = build_game_map(output)
        print("MAX SCORE:", MAX_SCORE)
        print("Remaining blocks:", len(game_map[game_map == 2]))


