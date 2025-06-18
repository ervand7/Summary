package main

import "fmt"

// If map is not initialized we can still check the existence of key

func main() {
	var m map[int]int
	val, ok := m[1]
	fmt.Println(val, ok) // 0 false
}
