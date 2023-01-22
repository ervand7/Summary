package main

import "fmt"

// If map is not initialized we can still check existence of key

func main() {
	var m map[int]string
	_, ok := m[1]
	fmt.Println(ok) // false
}
