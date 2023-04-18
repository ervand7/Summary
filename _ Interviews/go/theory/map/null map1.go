package main

import "fmt"

// unlike python we can refer to a non-existent key and get it zero value.
// Even if map is not initialized

func main() {
	var m map[int]int
	fmt.Println(m[992] == 0) // true
	fmt.Println(m[992])      // 0
}
