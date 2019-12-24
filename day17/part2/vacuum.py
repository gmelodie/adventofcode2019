import sys
import numpy as np
import time
import intcode


turn_right = {
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (-1, 0): (0, 1),
}

turn_left = {
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
    (0, -1): (1, 0),
    (1, 0): (0, 1),
}


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


def is_valid(maze, pos):
    if pos[0] < 0 or pos[0] >= maze.shape[0] or \
            pos[1] < 0 or pos[1] >= maze.shape[1]:
        return False

    if maze[pos[0]][pos[1]] != '#':
        return False

    return True


def find_path(maze, startpos):

    path = ['R', 0]
    pos = startpos
    direction = (0, 1) # initial direction set to RIGHT
    steps = 0

    while True:
        nxtpos = tuple(map(sum, zip(pos, direction)))
        if is_valid(maze, nxtpos):
            pos = nxtpos
            path[-1] += 1

        else:
            try_right = turn_right[direction]
            nxtpos = tuple(map(sum, zip(pos, try_right)))
            if is_valid(maze, nxtpos):
                direction = try_right
                pos = nxtpos
                path.append('R')
                path.append(1)
            else:
                try_left = turn_left[direction]
                nxtpos = tuple(map(sum, zip(pos, try_left)))
                if is_valid(maze, nxtpos):
                    direction = try_left
                    pos = nxtpos
                    path.append('L')
                    path.append(1)
                else:
                    break

    return path


def get_startpos(maze):
    startpos = (-1, -1)
    for i in range(maze.shape[0]):
        if startpos != (-1, -1):
            break
        for j in range(maze.shape[1]):
            if maze[i][j] == '^':
                startpos = (i, j)
                break
    return startpos


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
    startpos = get_startpos(maze)
    print(find_path(maze, startpos))

    seq = "A,B,A,C,A,B,C,B,C,B"
    A = "R,8,L,10,L,12,R,4"
    B = "R,8,L,12,R,4,R,4"
    C = "R,8,L,10,R,8"
    ans = [ord(a) for a in '\n'.join([seq, A, B, C])]
    ans.append(ord('\n'))
    ans.append(ord('n'))
    ans.append(ord('\n'))

    intcode.OUTPUT = []
    instructions[0] = 2 # wake up robot

    idx = rboffset = 0
    idx, rboffset = intcode.execute(instructions, \
                                    startidx=idx, \
                                    rboffset=rboffset, \
                                    inputdata=ans)

    for c in intcode.OUTPUT:
        if c == 10:
            print()
        else:
            print(chr(c), end='')

    print()
    print(intcode.RETVAL)
