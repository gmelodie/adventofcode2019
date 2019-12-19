import sys
import numpy as np
import intcode


def is_intersection(maze, pos):
    i, j = pos
    if maze[i][j+1] == maze[i][j-1] == '#' and \
            maze[i+1][j] == maze[i-1][j] == '#' and \
            maze[i][j] == '#':
        return True
    return False


def find_intersections(maze):
    intersections = []

    for i in range(1, maze.shape[0]-1):
        for j in range(1, maze.shape[1]-1):
            if is_intersection(maze, (i, j)):
                intersections.append((i,j))

    return intersections


def turn(maze, pos, direction, visited):
    nextpos = tuple(map(sum, zip(pos, directions[d])))
    if maze[nextpos[0]][nextpos[1]] == '#' and \
            nextpos not in visited:
        return nextpos

    return (-1, -1)



def find_path(maze, startpos):
    path = []
    visited = {}


    print(startpos)

    pos = startpos
    direction = 'UP'
    nsteps = 0

    while True:
        if pos == (-1, -1):
            break
        if nsteps == 1:
            path.append(direction)

        nextpos = tuple(map(sum, zip(pos, directions[direction])))
        if maze[nextpos[0]][nextpos[1]] == '#' and \
                nextpos not in visited:
            pos = nextpos
        else:
            pos = turn(maze, pos, direction, visited)


    return []


def generate_input(maze):
    startpos = (-1, -1)
    for i in range(maze.shape[0]):
        if startpos != (-1, -1):
            break
        for j in range(maze.shape[1]):
            if maze[i][j] == '^':
                startpos = (i, j)
                break
    path = find_path(maze, startpos)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 vacuum.py <instructions_file>")
        exit(1)

    instructions = intcode.load_instructions(sys.argv[1])
    idx, rboffset = intcode.execute(instructions.copy())

    maze = []
    row = []
    for c in intcode.OUTPUT:
        if c == 10:
            maze.append(row)
            row = []
            print()
        else:
            row.append(chr(c))
            print(chr(c), end='')

    maze.pop(-1) # remove empty row
    maze = np.array(maze)

    # Part 1
    # intersections = find_intersections(maze)
    # print(intersections)
    # print(sum(inter[0]*inter[1] for inter in intersections))

    # Part2
    inp = generate_input(maze)
    intcode.OUTPUT = []
    instructions[0] = 2 # wake up robot
    idx, rboffset = intcode.execute(instructions, \
                                    inputdata=inp)

