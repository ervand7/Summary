package main

import "fmt"

func main() {
	var i int
	if true {
		i := 7
		fmt.Print(i)
	}
	fmt.Print(i)
}
