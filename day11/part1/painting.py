import sys
import numpy as np
import intcode

def turn_right(direction):
    if direction == "up":
        return "right"
    elif direction == "right":
        return "down"
    elif direction == "down":
        return "left"
    elif direction == "left":
        return "up"


def turn_left(direction):
    if direction == "up":
        return "left"
    elif direction == "right":
        return "up"
    elif direction == "down":
        return "right"
    elif direction == "left":
        return "down"


def move(pos, direction):
    new_pos = pos
    if direction == "up":
        new_pos[0] -= 1
    elif direction == "right":
        new_pos[1] += 1
    elif direction == "down":
        new_pos[0] += 1
    elif direction == "left":
        new_pos[1] -= 1

    if new_pos[0] < 0 or new_pos[1] < 0:
        print("error: unexpected position", new_pos)
        exit(2)

    return new_pos


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 painting.py <intcode_file>")
        exit(1)

    pos = [500,500]
    direction = "up"
    painted = np.zeros((1000,1000))
    panel = np.zeros((1000,1000))
    instructions = intcode.load_instructions(sys.argv[1])

    idx = -1
    new_idx = 0
    while True:
        intcode.OUTPUT = []
        idx = new_idx
        new_idx = intcode.execute(instructions, startidx=idx, \
                          inputdata=[panel[pos[0]][pos[1]]])

        if idx == new_idx:
            break

        # paint current position
        color = intcode.OUTPUT[0]
        painted[pos[0]][pos[1]] = 1
        panel[pos[0]][pos[1]] = color

        # move to next position
        turn_dir = intcode.OUTPUT[1]
        if turn_dir == 0:
            direction = turn_left(direction)
        elif turn_dir == 1:
            direction = turn_right(direction)
        pos = move(pos, direction)

    unique, counts = np.unique(painted, return_counts=True)
    print(dict(zip(unique, counts)))
