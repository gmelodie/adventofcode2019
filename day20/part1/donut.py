import sys
import numpy as np


if __name__ == "__main__":
    maze = []
    for line in sys.stdin:
        maze.append(line.strip('\n'))
    maze = np.array(maze)
    print(maze)

    startpos = find_pos('AA')
    endpos = find_pos('ZZ')

    queue = [startpos]

    while queue:
        pos = queue.pop(0)
