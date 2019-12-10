package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type instruction struct {
	opcode  int
	nparams int
	name    string
}

var instructionTypes = map[int]instruction{
	1:  {1, 3, "sum"},
	2:  {2, 3, "mult"},
	3:  {3, 1, "input"},
	4:  {4, 1, "output"},
	5:  {5, 2, "jump-if-true"},
	6:  {6, 2, "jump-if-false"},
	7:  {7, 3, "less than"},
	8:  {8, 3, "equals"},
	99: {99, 0, "halt"},
}

func exec(instructions []int, IP int) int {
	params := getParams(instructions, IP)
	modes := getModes(instructions, IP)
}

// Run a sequence of instructions
func Run(instructions []int) []int {
	newIP := 0
	IP := 1

	for IP != newIP {
		IP = newIP
		newIP := exec(IP, instructions)
	}

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

// LoadRaw reads an intcode program from stdin
// and saves it to strip and the instructions to
// an array of instrucitons
func LoadRaw(rawText string) []int {
	var strip []int

	line := strings.Split(rawText, ",")
	for i := 0; i < len(line); i++ {
		intnum, _ := strconv.Atoi(line[i])
		strip = append(strip, intnum)
	}

	return strip
}

func main() {

	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()

	strip := LoadRaw(scanner.Text())

	endStrip := execStrip(instructions)

	fmt.Println(endStrip[0])
}
