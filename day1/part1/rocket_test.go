package main

import "testing"

func TestCalcFuel(t *testing.T) {
	// mass divisible by 3
	div := calcFuel(12)
	if div != 2 {
		t.Errorf("calcFuel failed, expected %d, got %d", 2, div)
	}

	// mass not divisible by 3
	nonDiv := calcFuel(14)
	if nonDiv != 2 {
		t.Errorf("calcFuel failed, expected %d, got %d", 2, nonDiv)
	}

	// big mass
	big := calcFuel(100756)
	if big != 33583 {
		t.Errorf("calcFuel failed, expected %d (%T), got %d(%T)",
			33583, 33583, big, big)
	}

	// another big mass
	big2 := calcFuel(1969)
	if big2 != 654 {
		t.Errorf("calcFuel failed, expected %d (%T), got %d(%T)",
			1969, 1969, big2, big2)
	}
}
