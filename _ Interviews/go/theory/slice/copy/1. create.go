package main

import "fmt"

// Скопируется столько элементов, сколько может вместить dst
// После copy адрес не меняется

func main() {
	a := []int{1, 2, 3, 4, 5}
	b := make([]int, 5)
	var c []int
	d := make([]int, 10)

	fmt.Printf("%p\n", &a) // 0x140000b8000
	fmt.Printf("%p\n", &b) // 0x140000b8018
	fmt.Printf("%p\n", &c) // 0x140000b8030
	fmt.Printf("%p\n", &d) // 0x140000b8048

	copy(b, a)
	copy(c, a)
	copy(d, a)

	fmt.Println(a) // [1 2 3 4 5]
	fmt.Println(b) // [1 2 3 4 5]
	fmt.Println(c) // []
	fmt.Println(d) // [1 2 3 4 5 0 0 0 0 0]

	fmt.Printf("%p\n", &a) // 0x140000b8000
	fmt.Printf("%p\n", &b) // 0x140000b8018
	fmt.Printf("%p\n", &c) // 0x140000b8030
	fmt.Printf("%p\n", &d) // 0x140000b8048
}
