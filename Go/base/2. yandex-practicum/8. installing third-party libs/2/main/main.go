package main

import (
	"fmt"

	"github.com/ervand7/go_adder"
)

func main() {
	if sum := go_adder.Add(1, 2); sum != 3 {
		panic(fmt.Sprintf("sum expected to be 3; got %d", sum))
	}

	fmt.Println("Well done!")
}
