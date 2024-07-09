// val will not be changed, because we reinitialized new

package main

import (
	"fmt"
)

var (
	A = 1
	B = "Hello"
	C = []int{1, 2, 3}
	D = map[int]string{1: "1"}
)

func changeVal() {
	A := 888
	fmt.Printf("%p\n", &A) // 0x140000ac008

	B := "world"
	fmt.Printf("%p\n", &B) // 0x14000096020

	C := []int{4, 5, 6}
	fmt.Printf("%p\n", &C) // 0x140000a0018

	D := map[int]string{2: "2"}
	fmt.Printf("%p\n", &D) // 0x140000a6020
}

func main() {
	fmt.Printf("%p\n", &A) // 0x100b503a8
	fmt.Printf("%p\n", &B) // 0x100b611f0
	fmt.Printf("%p\n", &C) // 0x100b613a0
	fmt.Printf("%p\n", &D) // 0x100b67ee0

	changeVal()

	fmt.Println(A) // 1
	fmt.Println(B) // Hello
	fmt.Println(C) // [1 2 3]
	fmt.Println(D) // [1 2 3]
}
