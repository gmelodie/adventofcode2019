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

	// Brute force verb and noun values
	expected := 19690720
	endStrip := make([]int, len(instructions))
	for i := 0; i < 100; i++ {
		for j := 0; j < 100; j++ {
			copy(endStrip, instructions)
			endStrip[1] = i // noun
			endStrip[2] = j // verb
			endStrip = execStrip(endStrip)
			if endStrip[0] == expected {
				fmt.Println("noun == ", endStrip[1])
				fmt.Println("verb == ", endStrip[2])
				answer := 100*endStrip[1] + endStrip[2]
				fmt.Println("100 * noun + verb == ", answer)
				return
			}
		}
	}

}
