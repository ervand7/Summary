package main

import (
	"fmt"
)

// val will be changed because after assigning new val vars will keep the same addr

var (
	a = 1
	b = "Hello"
	c = []int{1, 2, 3}
	d = map[int]string{1: "1"}
)

func change() {
	a = 888
	fmt.Printf("%p\n", &a) // 0x1029043a8

	b = "world"
	fmt.Printf("%p\n", &b) // 0x1029151f0

	c = []int{4, 5, 6}
	fmt.Printf("%p\n", &c) // 0x1029153a0

	d = map[int]string{2: "2"}
	fmt.Printf("%p\n", &d) // 0x10291bee0
}

func main() {
	fmt.Printf("%p\n", &a) // 0x1029043a8
	fmt.Printf("%p\n", &b) // 0x1029151f0
	fmt.Printf("%p\n", &c) // 0x1029153a0
	fmt.Printf("%p\n", &d) // 0x10291bee0

	change()

	fmt.Println(a) // 888
	fmt.Println(b) // world
	fmt.Println(c) // [4 5 6]
	fmt.Println(d) // map[2:2]
}
