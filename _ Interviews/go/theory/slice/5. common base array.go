package main

import "fmt"

// оставшиеся значения (:cap(b)) берутся из базового массива

func main() {
	a := make([]int, 6, 6)
	fmt.Printf("%p\n", a) // 0x14000122000
	for i := 0; i < len(a); i++ {
		a[i] = i
	}
	fmt.Println(a) // [0 1 2 3 4 5]

	b := a[1:3]
	fmt.Printf("%p\n", b) // 0x14000122008
	fmt.Println(b)        // [1 2]
	fmt.Println(cap(b))   // 5

	b = b[:cap(b)]
	fmt.Printf("%p\n", b) // 0x14000122008
	fmt.Println(b)        // [1 2 3 4 5]

	fmt.Println(len(a), cap(a)) // 6 6
	fmt.Println(len(b), cap(b)) // 5 5
}
