package main

import "fmt"

func main() {
	i := 0
	defer fmt.Println(i)

	i += 3
	fmt.Println(i)

	i += 1
}

/*
3
0
*/
