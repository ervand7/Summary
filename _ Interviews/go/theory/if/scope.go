package main

import "fmt"

// if we use `:=` in `if` scope, there will be created a new variable

func main() {
	var i int
	if true {
		i := 7
		fmt.Print(i)
	}
	fmt.Print(i)
}

// 70
