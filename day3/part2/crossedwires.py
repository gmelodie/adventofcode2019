


def visit_path(visited, path):
    pos = [0,0]
    step = 0

    for (direction, distance) in path:
        for i in range(distance):
            step += 1
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

            if (pos[0], pos[1]) not in visited:
                visited[(pos[0], pos[1])] = step

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

    # Find position with fewest combined steps
    # from (0,0) that has been visited by both wires
    minsteps = 100000000
    minpos = [-1, -1]
    for pos in visited1.keys():
        if pos in visited2:
            print(pos)
            auxsteps = visited1[pos] + visited2[pos]
            if auxsteps < minsteps:
                minsteps = auxsteps
                minpos = pos

    print("----------------")
    print(minpos, minsteps)
