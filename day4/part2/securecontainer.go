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

	// Have *exatly* two adjacent digits
	adjacent := []int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
	for i := 0; i < len(lstPasswd)-1; i++ {
		if lstPasswd[i] == lstPasswd[i+1] {
			adjacent[int(lstPasswd[i]-'0')]++
		}
	}

	for _, adj := range adjacent {
		if adj == 1 {
			return true
		}
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
