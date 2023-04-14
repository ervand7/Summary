package main

import (
	"fmt"
	"math/rand"
)

// with test

type randGenerator interface {
	Intn(n int) int
}

type mockGenerator struct {
	counter int
}

func (m *mockGenerator) Intn(_ int) int {
	m.counter += 1
	duplicateValue := 777
	if m.counter == 1 || m.counter == 2 {
		return duplicateValue
	}
	return m.counter * m.counter
}

func nrand(n int, r randGenerator) []int {
	result := make([]int, 0, n)
	hTable := make(map[int]bool, n)
	for {
		randValue := r.Intn(n + 1)
		if _, ok := hTable[randValue]; !ok {
			result = append(result, randValue)
			hTable[randValue] = true
		}
		if len(result) == n {
			break
		}
	}

	return result
}

func testSuccessNrandDuplicateValues() string {
	failGenerator := &mockGenerator{}
	n := 10
	result := nrand(n, failGenerator)
	if len(result) != 10 {
		return "fail"
	}
	return "success"
}

func main() {
	r := rand.New(rand.NewSource(1))
	fmt.Println(nrand(10, r))
	fmt.Println(testSuccessNrandDuplicateValues())
}
