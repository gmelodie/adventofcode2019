package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func calcFuel(mass int) int {
	return (int(mass/3.0) - 2)
}

func main() {
	totalFuel := 0
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		mass, _ := strconv.Atoi(scanner.Text())
		totalFuel += calcFuel(mass)
	}

	fmt.Println(totalFuel)

	if err := scanner.Err(); err != nil {
		log.Println(err)
	}
}
