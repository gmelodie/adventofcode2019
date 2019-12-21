import sys
import heapq
import numpy as np


def find_possible_moves(cost, maze, pos, doors):
    moves = []
    # Find reachable keys
    # Alter maze (remove key and respective door)
    # Update pos (now it is the last removed key's)
    # Update cost
    # Append tuple to moves
    return moves


if __name__ == "__main__":

    # Read input
    maze = []
    for line in sys.stdin:
        maze.append(list(line.strip()))
    maze = np.array(maze)

    # Find starting pos and doors
    startpos = (-1, -1)
    door_pos = {}
    ndoors = 0
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            if maze[i][j] == '@':
                startpos = (i, j)
            elif maze[i][j] != '#' and maze[i][j] != '.' and \
                maze[i][j] >= 'A' and maze[i][j] <= 'Z':
                ndoors += 1
                door = maze[i][j]
                door_pos[door] = (i, j)

    if startpos == (-1, -1):
        print("Couldn't find starting position '@'")
        exit(1)

    # if not doors:
    if ndoors <= 0:
        print("Didn't find any doors")
        exit(2)

    print("Startpos:", startpos)
    print("Doors:", door_pos)
    print("Ndoors:", ndoors)

    # Find best (shortest) path
    pos = startpos
    doors = 0
    cost = 0
    possibilities = []
    while doors < ndoors:
        # Find next possible moves
        # List of (cost, maze, pos, ndoors)
        moves = find_possible_moves(cost, maze.copy(), pos, doors)

        for move in moves:

            # Insert (cost, maze, pos, doors) in heap
            heapq.heappush(possibilities, move)

        # Get (cost, maze, pos, doors) from heap
        cost, maze, pos, doors = heapq.heappop(possibilities)

    # Print shortest path cost (length)
    print(cost)
