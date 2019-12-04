package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type coord struct {
	x int
	y int
}

type move struct {
	direction rune
	distance  int
}

func parseMoves(text []string) []move {
	allMoves := make([]move, len(text))
	for i, strmv := range text {
		dist, _ := strconv.Atoi(strmv[1:])
		mv := move{rune(strmv[0]), dist}
		allMoves[i] = mv
	}
	return allMoves
}

func readInput() ([]move, []move) {
	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	path1 := parseMoves(strings.Split(scanner.Text(), ","))

	scanner.Scan()
	path2 := parseMoves(strings.Split(scanner.Text(), ","))

	return path1, path2
}

func visit(path []move) map[coord]int {
	visited := make(map[coord]int)
	pos := coord{0, 0}
	steps := 0

	for _, mv := range path {
		for i := 0; i < mv.distance; i++ {
			steps++

			switch mv.direction {
			case 'U':
				pos.y++
			case 'D':
				pos.y--
			case 'L':
				pos.x--
			case 'R':
				pos.x++
			}

			if !inVisited(pos, visited) {
				visited[pos] = steps
			}

		}
	}

	return visited
}

func manhattanDist(pos1, pos2 coord) int {
	return int(math.Abs(float64(pos1.x-pos2.x)) + math.Abs(float64(pos1.y-pos2.y)))
}

func inVisited(pos coord, visited map[coord]int) bool {
	if _, ok := visited[pos]; ok {
		return true
	}
	return false
}

func main() {
	path1, path2 := readInput()

	visited1 := visit(path1)
	visited2 := visit(path2)

	// Calc closest pos visited by both wires
	minpos := coord{0, 0}
	minsteps := 100000000
	for pos, auxsteps1 := range visited1 {
		if auxsteps2, ok := visited2[pos]; ok && minsteps > auxsteps1+auxsteps2 {
			minsteps = auxsteps1 + auxsteps2
			minpos = pos
		}
	}

	fmt.Println(minpos, minsteps)
}
