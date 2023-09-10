package main

// Требуется реализовать функцию uniqRandn, которая генерирует слайс длины n
// уникальных рандомных чисел.
import (
	"fmt"
	"math/rand"
)

func main() {
	fmt.Println(uniqRandn(10))
}

func uniqRandn(n int) []int {
	result := make([]int, 0, n)
	hTable := make(map[int]bool, n)
	for {
		randValue := rand.Int()
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
