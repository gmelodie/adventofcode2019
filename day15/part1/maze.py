import sys
import intcode

def update_pos(pos, direction):
    if direction == 1:
        return (pos[0], pos[1]+1)
    elif direction == 2:
        return (pos[0], pos[1]-1)
    elif direction == 3:
        return (pos[0]-1, pos[1])
    elif direction == 4:
        return (pos[0]+1, pos[1])


def bfs(instructions):
    visited = {}

    # queue: (instructions, idx, rboffset, pos, pathlen)
    queue = []
    visited[(0,0)] = True
    queue.append((instructions.copy(), 0, 0, (0,0), 0))

    while True:
        instr, idx, rboffset, pos, pathlen = queue.pop(0)
        # print(idx, rboffset, pos, pathlen)
        for i in range(1, 5):
            new_pos = update_pos(pos, i)
            if new_pos in visited:
                continue
            else:
                visited[new_pos] = True
            # print(pathlen)

            new_instr = instr.copy()
            new_idx, new_rboffset = intcode.execute(new_instr, \
                                            startidx=idx, \
                                            rboffset=rboffset,\
                                            inputdata=[i])
            output = intcode.RETVAL

            if output == 2:
                print(output)
                return pathlen+1
            elif output == 1:
                queue.append((new_instr, new_idx, new_rboffset, new_pos, pathlen+1))
            elif output == 0:
                continue


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 maze.py <instructions_file>")
        exit(1)

    instructions = intcode.load_instructions(sys.argv[1])
    print(bfs(instructions))



