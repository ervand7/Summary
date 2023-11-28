package main

import "fmt"

// по факту, выведет все числа, которые встречаются нечетное кол-во раз

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
	fmt.Println(hTable) // map[0:true 1:true 3:true 7:true]
}
