package main

import "fmt"

func changer(arr *[]int) {
	qwe := *arr
	qwe = append(qwe, 111)
	fmt.Println(qwe) // [0 1 2 3 4 111]
	fmt.Printf("%p\n%p\n", arr, &qwe)
	/*
	   0x1400011e018
	   0x1400011e048
	*/
}

func main() {
	a := make([]int, 0)
	a = append(a, 0, 1, 2, 3, 4)
	fmt.Println(a) // [0 1 2 3 4]

	changer(&a)
	fmt.Println(a) // [0 1 2 3 4]
}
