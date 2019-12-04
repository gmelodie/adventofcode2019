


def visit_path(visited, path):
    pos = [0,0]

    for (direction, distance) in path:
        for i in range(distance):
            if direction is 'R':
                pos[1] += 1
            elif direction is 'L':
                pos[1] -= 1
            elif direction is 'U':
                pos[0] += 1
            elif direction is 'D':
                pos[0] -= 1
            else:
                print("Undefined direction ", direction)
                exit(1)

            visited[(pos[0], pos[1])] = 1

    return visited


def manhattan_dist(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1-x2) + abs(y1-y2)


if __name__ == "__main__":
    # Read input
    path1 = [[list(move)[0], int(move[1:])] \
             for move in input().split(',')]

    path2 = [[list(move)[0], int(move[1:])] \
             for move in input().split(',')]

    # Mark visited positions
    # Same position can be visited twice by same wire
    # so we have two distinct lists of visited positions
    visited1 = visit_path({}, path1)
    visited2 = visit_path({}, path2)

    # Find closest position from (0,0) that has
    # been visited by both wires
    mindist = 100000000
    minpos = [-1, -1]
    for pos in visited1.keys():
        if pos in visited2:
            print(pos)
            auxdist = manhattan_dist(pos, (0,0))
            if auxdist < mindist:
                mindist = auxdist
                minpos = pos

    print("----------------")
    print(minpos, mindist)
