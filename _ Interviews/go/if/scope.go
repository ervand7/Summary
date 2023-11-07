package main

import "fmt"

// if we use `:=` in `if` scope, there will be created a new variable

func main() {
	var i int
	fmt.Printf("%p\n", &i) // 0x14000122008

	if true {
		i := 7
		fmt.Printf("%p\n", &i) // 0x14000122020
		fmt.Print(i)
	}
	fmt.Print(i)
}

// 70
