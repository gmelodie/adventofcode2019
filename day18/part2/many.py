import sys
import copy
import collections
import heapq
import numpy as np


directions = [(1,0), (0, 1), (-1, 0), (0, -1)]
cache = {}


def find_reachable_keys(maze, pos, havekeys):
    keys = {}
    bfs = collections.deque([pos])
    distance = {pos: 0}

    while bfs:
        pos = bfs.popleft()
        for d in directions:
            auxpos = (pos[0] + d[0], pos[1] + d[1])

            # Out of bounds
            if not (0 <= auxpos[0] < maze.shape[0] and \
                    0 <= auxpos[1] < maze.shape[1]):
                continue

            ch = maze[auxpos[0]][auxpos[1]]
            if ch == '#':
                continue
            if auxpos in distance:
                continue

            distance[auxpos] = distance[pos] + 1
            if 'A' <= ch <= 'Z' and ch.lower() not in havekeys:
                continue
            if 'a' <= ch <= 'z' and ch not in havekeys:
                keys[ch] = distance[auxpos], auxpos
            else:
                bfs.append(auxpos)

    return keys


def minwalk(maze, pos, havekeys):
    # Search in cache
    hks = ''.join(sorted(havekeys))
    if (pos, hks) in cache:
        return cache[pos, hks]

    # Find reachable keys
    # keys[keyname] = (distance, position)
    keys = find_reachable_keys(maze, pos, havekeys)
    if len(cache) % 10 == 0:
        print("hks:", hks, len(hks))

    if len(keys) == 0:
        return 0

    moves = []
    for ch, (dist, auxpos) in keys.items():
        heapq.heappush(moves, \
                       (dist + minwalk(maze, auxpos, \
                                       havekeys + ch)))
    ans = heapq.heappop(moves)
    cache[pos, hks] = ans
    return ans


if __name__ == "__main__":

    # Read input
    maze = []
    for line in sys.stdin:
        maze.append(list(line.strip()))
    maze = np.array(maze)

    # Find starting pos and doors
    startpos = (-1, -1)
    for i in range(maze.shape[0]):
        if startpos != (-1, -1):
            break
        for j in range(maze.shape[1]):
            if maze[i][j] == '@':
                startpos = (i, j)
                break

    if startpos == (-1, -1):
        print("Couldn't find starting position '@'")
        exit(1)

    print("Startpos:", startpos)

    print(minwalk(maze, startpos, ''))
