import sys
import intcode




if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 maze.py <instructions_file>")
        exit(1)

    instructions = intcode.load_instructions(sys.argv[1])

    print(instructions)
