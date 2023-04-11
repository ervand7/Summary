package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	fmt.Println(generateSlice(10))
}

func generateSlice(size int) []int {
	slice := make([]int, size)
	for i := 0; i < size; i++ {
		rand.Seed(time.Now().UnixNano())
		slice[i] = rand.Intn(999) - rand.Intn(999)
	}
	return slice
}
