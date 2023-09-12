package main

import "fmt"

// append можно применять с nil-слайсом

func main() {
	var a []int
	fmt.Printf("%p\n", a) // 0x0

	for i := 0; i < 10; i++ {
		a = append(a, i)
	}

	fmt.Println(a)        // [0 1 2 3 4 5 6 7 8 9]
	fmt.Printf("%p\n", a) // 0x1400012a000
}
