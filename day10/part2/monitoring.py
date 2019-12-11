import sys
import numpy as np


def inclination(coord1, coord2):
    if coord1[0] == coord2[0]: # vertical line (m = dy/0)
        return 1000 # return very specific number

    return (coord2[1]-coord1[1])/(coord2[0]-coord1[0])


def find_visible(base, asteroids_coord):
    visible = []
    visible_pos = []

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
            if entry not in visible:
                visible_pos.append(asteroid)
                visible.append(entry)

    print(base, len(visible))
    return visible, visible_pos


def station_pos(asteroids_coord):
    max_visible = set()
    max_coords = (-1, -1)
    for asteroid in asteroids_coord:
        visible, visible_pos = find_visible(asteroid, asteroids_coord)
        if len(visible) > len(max_visible):
            max_visible = visible
            max_visible_pos = visible_pos
            max_coords = asteroid
    return max_coords, max_visible, max_visible_pos


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

    station, visible, visible_pos = station_pos(asteroids_coord)

    print(visible)
    print(visible_pos)
    print(len(visible))
    print(station)

