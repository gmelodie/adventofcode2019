import sys
import numpy as np


directions = {
    'UP': (-1, 0),
    'DOWN': (1, 0),
    'RIGHT': (0, 1),
    'LEFT': (0, -1),
}

portals = {}

# Build dictionary of portals
def find_portals(maze):
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            pos, portal = portal_str(maze, (i, j))
            if not in_bounds(pos, maze):
                continue
            if portal == '':
                continue
            if portal in portals:
                if pos not in portals[portal]:
                    portals[portal].append(pos)
            else:
                portals[portal] = [pos]


# Return string of the portal in position pos
# return empty string if no portal is found
def portal_str(maze, pos):
    ch = maze[pos[0]][pos[1]]

    if ch < 'A' or 'Z' < ch:
        return (-1, -1), ''

    for direction in directions.keys():
        d = tuple(map(sum, zip(directions[direction], pos)))
        if not in_bounds(d, maze):
            continue
        ch2 = maze[d[0]][d[1]]

        portal_string = ''
        portal_pos = (-1, -1)

        if 'A' <= ch2 <= 'Z':
            if direction == 'UP':
                portal_pos = (d[0]-2, d[1])
                portal_string = ch2 + ch
            elif direction == 'DOWN':
                portal_pos = (d[0]+2, d[1])
                portal_string = ch + ch2
            elif direction == 'LEFT':
                portal_pos = (d[0], d[1]-2)
                portal_string = ch2 + ch
            elif direction == 'RIGHT':
                portal_pos = (d[0], d[1]+2)
                portal_string = ch + ch2

    return portal_pos, portal_string


# Return exit position of a portal,
# return same position if AA or ZZ
def teleport(maze, pos):
    inpos, portal = portal_str(maze, pos)
    pos1, pos2 = portals[portal]

    if pos1 == inpos:
        return pos2

    return pos1


def in_bounds(pos, maze):
    if 0 <= pos[0] < maze.shape[0] and 0 <= pos[1] < maze.shape[1]:
        return True
    return False


if __name__ == "__main__":
    maze = []
    for line in sys.stdin:
        maze.append(np.array(list(line.strip('\n'))))
    maze = np.array(maze)
    print(maze)
    print(maze.shape)

    find_portals(maze)
    print(portals)

    startpos = portals['AA'][0]
    endpos = portals['ZZ'][0]

    print(startpos, endpos)

    queue = [(0, startpos)]
    visited = {}

    while queue:
        dist, pos = queue.pop(0)

        if pos in visited or not in_bounds(pos, maze):
            continue

        visited[pos] = dist
        ch = maze[pos[0]][pos[1]]

        if ch == '#' or ch == ' ':
            continue
        elif ch == '.':
            queue.append(dist+1, tuple(map(sum, zip(directions['UP'], pos))))
            queue.append(dist+1, tuple(map(sum, zip(directions['DOWN'], pos))))
            queue.append(dist+1, tuple(map(sum, zip(directions['LEFT'], pos))))
            queue.append(dist+1, tuple(map(sum, zip(directions['RIGHT'], pos))))
        else: #portal
            if pos in portals['ZZ']:
                print(dist)
                break
            newpos = teleport(maze, pos)
            queue.append(dist+1, newpos)

    print(pos)
    print(dist)







