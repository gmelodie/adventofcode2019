import sys
import math
import numpy as np


def inclination(coord1, coord2):
    if coord1[0] == coord2[0]: # vertical line (m = dy/0)
        return 3.141234 # return very specific number

    return (coord2[1]-coord1[1])/(coord2[0]-coord1[0])


def dist(a, b):
    return math.sqrt((a[1]-b[1])**2 + (a[0] - b[0])**2)


def find_visible(base, asteroids_coord):
    aux = set()
    visited = {}

    for asteroid in asteroids_coord:
        if asteroid != base:
            m = inclination(base, asteroid)
            # differ from asteroids in same line (before and after)
            if asteroid[0] < base[0]:
                entry = (m, -1)
            elif asteroid[0] > base[0]:
                entry = (m, 1)
            elif asteroid[0] == base[0]:
                if asteroid[1] < base[1]:
                    entry = (m, -1)
                elif asteroid[1] > base[1]:
                    entry = (m, 1)
                elif asteroid[1] == base[1]:
                    print("error:should not get here")

            if entry in aux and \
                dist(visited[entry], base) > dist(base, asteroid):
                visited[entry] = asteroid
            elif entry not in aux:
                aux.add(entry)
                visited[entry] = asteroid


    return visited.values()


def get_angle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - \
                       math.atan2(a[1]-b[1], a[0]-b[0]))
    angle = abs(ang)
    print(angle)
    return angle


def get_slope(pos):
    orig_x = max_coords[0]
    orig_y = max_coords[1]
    x = pos[0]
    y = pos[1]

    a = pos
    b = max_coords
    c = (max_coords[0], 0)
    angle = get_angle(a, b, c)

    # Need to apply an offset depending on quadrant
    if x >= orig_x:
        if y <= orig_y:
            # first quadrant
            pass
        elif y > orig_y:
            # second quadrant
            pass
    elif x < orig_x:
        if y > orig_y:
            # third quadrant
            angle = 360 - angle
        elif y <= orig_y:
            # fourth quadrant
            angle = 360 - angle


    print(pos, max_coords, c, angle)
    return angle

if __name__ == '__main__':
    asteroids_coord = []
    spacemap = []
    for line in sys.stdin:
        spacemap.append(list(line.strip()))
    spacemap = np.array(spacemap)

    for i in range(spacemap.shape[0]):
        for j in range(spacemap.shape[1]):
            if spacemap[i][j] == '#':
                # x == j (cols) and y == i (rows)
                asteroids_coord.append((j, i))

    max_visible = []
    global max_coords
    max_coords = (-1, -1)
    for asteroid in asteroids_coord:
        visible = find_visible(asteroid, asteroids_coord)
        if len(visible) > len(max_visible):
            max_visible = visible
            max_coords = asteroid

    max_visible = sorted(max_visible, key=get_slope)

    print(max_visible)
    print(max_visible[199])
    print(max_coords, '->', len(max_visible))

