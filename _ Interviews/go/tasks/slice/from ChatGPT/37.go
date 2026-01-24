package main

import "fmt"

func main() {
	m := map[string][]int{"a": {1, 2, 3, 4}}
	v := m["a"]
	v = append(v[:2:2], 9, 10)

	fmt.Println(m["a"])
	fmt.Println(v)
}
