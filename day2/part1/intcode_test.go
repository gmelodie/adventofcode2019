package main

import "testing"

func TestExecStrip(t *testing.T) {
	expected := []int{2, 0, 0, 0, 99}
	actual := execStrip([]int{1, 0, 0, 0, 99})
	if expected != actual {
		t.Errorf("Expected %q, got %q", expected, actual)
	}
}
