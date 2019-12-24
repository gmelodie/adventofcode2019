import sys
import numpy as np
import intcode


def find_intersections(maze):
    intersections = []

    for i in range(1, maze.shape[0]-1):
        for j in range(1, maze.shape[1]-1):
            if maze[i][j+1] == maze[i][j-1] == '#' and \
                    maze[i+1][j] == maze[i-1][j] == '#' and \
                    maze[i][j] == '#':
                intersections.append((i,j))

    return intersections


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 vacuum.py <instructions_file>")
        exit(1)

    instructions = intcode.load_instructions(sys.argv[1])
    idx, rboffset = intcode.execute(instructions)

    maze = []
    row = []
    for i, c in enumerate(intcode.OUTPUT):
        if c == 10:
            maze.append(row)
            row = []
            print()
        else:
            row.append(chr(c))
            print(chr(c), end='')

    maze.pop(-1) # remove empty row
    # print(maze)
    maze = np.array(maze)
    print(maze.shape)

    intersections = find_intersections(maze)
    print(intersections)

    s = sum(inter[0]*inter[1] for inter in intersections)
    print(s)


