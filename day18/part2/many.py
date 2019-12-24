import sys
import copy
import collections
import heapq
import numpy as np


directions = [(1,0), (0, 1), (-1, 0), (0, -1)]
left = {
    (1,0): (0, 1),
    (-1,0): (0, -1),
    (0,1): (-1, 0),
    (0,-1): (1, 0),
}

right = {
    (1,0): (0, -1),
    (-1,0): (0, 1),
    (0,1): (1, 0),
    (0,-1): (-1, 0),
}

cache = {}


def find_reachable_keys(maze, pos, havekeys):
    keys = {}
    bfs = collections.deque([pos])
    distance = {}
    for p in pos:
        distance[p] = 0

    while bfs:
        pos = bfs.popleft()
        for d in directions:
            aux4pos = [(p[0] + d[0], p[1] + d[1]) for p in pos]
            for i, auxpos in enumerate(aux4pos):
                newpos = pos.copy()
                newpos[i] = auxpos
                # Out of bounds
                if not (0 <= auxpos[0] < maze.shape[0] and \
                        0 <= auxpos[1] < maze.shape[1]):
                    continue

                ch = maze[auxpos[0]][auxpos[1]]
                if ch == '#':
                    continue
                if auxpos in distance:
                    continue

                distance[auxpos] = distance[pos[i]] + 1
                if 'A' <= ch <= 'Z' and ch.lower() not in havekeys:
                    continue
                if 'a' <= ch <= 'z' and ch not in havekeys:
                    keys[ch] = distance[auxpos], newpos
                else:
                    bfs.append(newpos)

    return keys


def minwalk(maze, pos, havekeys):
    # Search in cache
    hks = ''.join(sorted(havekeys))
    pos1, pos2, pos3, pos4 = pos
    if (pos1, pos2, pos3, pos4, hks) in cache:
        return cache[pos1, pos2, pos3, pos4, hks]

    # Find reachable keys
    # keys[keyname] = (distance, position)
    keys = find_reachable_keys(maze, pos, havekeys)
    if len(cache) % 10 == 0:
        print("hks:", hks, len(hks))

    if len(keys) == 0:
        return 0

    moves = []
    for ch, (dist, newpos) in keys.items():
        heapq.heappush(moves, \
                       (dist + minwalk(maze, newpos, \
                                       havekeys + ch)))
    ans = heapq.heappop(moves)
    cache[pos1, pos2, pos3, pos4, hks] = ans
    return ans


if __name__ == "__main__":

    # Read input
    maze = []
    for line in sys.stdin:
        maze.append(list(line.strip()))
    maze = np.array(maze)

    # Find starting pos
    startpos = []
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            if maze[i][j] == '@':
                startpos.append((i, j))

    if len(startpos) == 0:
        print("Couldn't find starting position '@'")
        exit(1)

    print("Startpos:", startpos)

    print(minwalk(maze, startpos, ''))
