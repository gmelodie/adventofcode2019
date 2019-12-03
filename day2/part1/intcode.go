package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var instructions []int

	// Read input
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()

	line := strings.Split(scanner.Text(), ",")
	for _, num := range line {
		intnum, _ := strconv.Atoi(num)
		instructions = append(instructions, intnum)
	}

	// Calculate stuff
	instructions[1] = 12
	instructions[2] = 2

	idx := 0

	for opcode := instructions[idx]; opcode != 99; opcode = instructions[idx] {
		if opcode == 1 {
			instructions[idx+3] = instructions[idx+1] + instructions[idx+2]
		} else if opcode == 2 {
			instructions[idx+3] = instructions[idx+1] * instructions[idx+2]
		} else {
			fmt.Printf("Unexpected opcode %d\n", opcode)
			os.Exit(1)
		}

		idx += 4
	}

	fmt.Println(instructions[0])
}
