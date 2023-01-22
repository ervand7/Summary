package main

import "fmt"

// the element will change for both slices, because they have the same base array

func main() {
	a := make([]int, 6, 6)
	for i := 0; i < len(a); i++ {
		a[i] = i
	}

	b := a[1:3]
	b[0] = 777
	fmt.Println(a) // [0 777 2 3 4 5]
	fmt.Println(b) // [777 2]
}
