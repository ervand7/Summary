package main

import "fmt"

// в отличие от python адреса остаются теми же

func main() {
	a := 1
	fmt.Printf("%p\n", &a) // 0x140000a6018
	a = 12
	fmt.Printf("%p\n", &a) // 0x140000a6018

	b := "1"
	fmt.Printf("%p\n", &b) // 0x1400008e050
	b = "12"
	fmt.Printf("%p\n", &b) // 0x1400008e050
}