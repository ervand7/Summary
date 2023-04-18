package main

import "fmt"

// the element will change for both slices

func main() {
	a := make([]int, 6, 6)
	for i := 0; i < len(a); i++ {
		a[i] = i
	}

	b := a[1:3]
	fmt.Println(a)        // [0 1 2 3 4 5]
	fmt.Println(b)        // [1 2]
	fmt.Printf("%p\n", a) // 0x14000124030
	fmt.Printf("%p\n", b) // 0x14000124038

	b[0] = 777
	fmt.Println(a) // [0 777 2 3 4 5]
	fmt.Println(b) // [777 2]
}
