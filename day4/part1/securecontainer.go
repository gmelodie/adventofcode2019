package main

import (
	"fmt"
	"strconv"
)

func validate(passwd, start, end int) bool {
	lstPasswd := []rune(strconv.Itoa(passwd))

	// Is a six-digit number
	if len(lstPasswd) != 6 {
		return false
	}

	// Within the range [start, end] inclusive
	if passwd < start || passwd > end {
		return false
	}

	// Digits never decrease
	for i := 0; i < len(lstPasswd)-1; i++ {
		if lstPasswd[i] > lstPasswd[i+1] {
			return false
		}
	}

	// Have two adjacent digits
	adjacent := false
	for i := 0; i < len(lstPasswd)-1; i++ {
		if lstPasswd[i] == lstPasswd[i+1] {
			adjacent = true
		}
	}

	if adjacent {
		return true
	}

	return false
}

func main() {
	start := 307237
	end := 769058

	validPasswds := 0
	for i := start; i <= end; i++ {
		if validate(i, start, end) {
			validPasswds++
		}
	}
	fmt.Println(validPasswds)
}
