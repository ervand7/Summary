package main

import "fmt"

/*
map in go is not ordered.
*/

func main() {
	m := map[int]string{
		1: "a",
		2: "b",
		3: "c",
		4: "d",
	}

	for k, v := range m {
		fmt.Println(k, v)
	}
	/*
		3 c
		4 d
		1 a
		2 b
	*/

	for k := range m {
		fmt.Println(k)
	}
	/*
		2
		3
		4
		1
	*/

	fmt.Println(m) // map[1:a 2:b 3:c 4:d]
}
