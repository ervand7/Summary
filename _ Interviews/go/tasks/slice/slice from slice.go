package main

import "fmt"

func main() {
	a := []string{"x", "y", "z"}
	b := a[1:2]
	fmt.Println(b)

	b[0] = "q"
	fmt.Println(a)
}
