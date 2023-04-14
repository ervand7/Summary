package main

import "fmt"

func main() {
	a := []int{1, 2, 3, 2, 1, 3, 3, 1, 7, 22, 22, 0, 0, 0, 0, 0}
	hTable := make(map[int]bool)

	for _, val := range a {
		if _, ok := hTable[val]; !ok {
			hTable[val] = true
		} else {
			delete(hTable, val)
		}
	}

	// выведет все значения, которые без пар
	fmt.Println(hTable)
}
