package main

func readInput() {
}

func main() {
	path1 := readInput()
	path2 := readInput()

	visited1 := checkVisited(path1)
	visited2 := checkVisited(path2)

	// Calc closest pos visited by both wires
	minpos := origin
	mindist := 0
	for i, pos := range visited1 {
		if auxdist := manhattanDist(origin, pos); inVisited(pos, visited2) && mindist > auxdist {
			mindist = auxdist
			minpos = pos
		}
	}
}
