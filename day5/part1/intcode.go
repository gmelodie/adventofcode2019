package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func execStrip(instructions []int) []int {
	idx := 0

	for opcode := instructions[idx]; opcode != 99; opcode = instructions[idx] {
		a := instructions[idx+1]
		b := instructions[idx+2]
		i := instructions[idx+3]
		if opcode == 1 {
			instructions[i] = instructions[a] + instructions[b]
		} else if opcode == 2 {
			instructions[i] = instructions[a] * instructions[b]
		} else {
			fmt.Printf("Unexpected opcode %d\n", opcode)
			os.Exit(1)
		}

		idx += 4
	}

	return instructions
}

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

	endStrip := execStrip(instructions)

	fmt.Println(endStrip[0])
}
