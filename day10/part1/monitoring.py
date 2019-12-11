import sys
import numpy as np


def inclination(coord1, coord2):
    if coord1[0] == coord2[0]: # vertical line (m = dy/0)
        return 3.141234 # return very specific number

    return (coord2[1]-coord1[1])/(coord2[0]-coord1[0])


def find_visible(base, asteroids_coord):
    visible = set()

    for asteroid in asteroids_coord:
        if asteroid != base:
            m = inclination(base, asteroid)
            # differ from asteroids in same line (before and after)
            if asteroid[0] < base[0]:
                visible.add((m, -1))
            elif asteroid[0] > base[0]:
                visible.add((m, 1))
            elif asteroid[0] == base[0]:
                if asteroid[1] < base[1]:
                    visible.add((m, -1))
                elif asteroid[1] > base[1]:
                    visible.add((m, 1))
                elif asteroid[1] == base[1]:
                    print("error:should not get here")

    print(base, len(visible))
    return len(visible)


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

    max_visible = 0
    max_coords = (-1, -1)
    for asteroid in asteroids_coord:
        visible = find_visible(asteroid, asteroids_coord)
        if visible > max_visible:
            max_visible = visible
            max_coords = asteroid

    #print(spacemap)
    print(asteroids_coord)
    print(max_visible)
    print(max_coords)

