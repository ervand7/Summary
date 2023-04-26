package main

import "fmt"

func main() {
	m1 := make(map[string]string, 5)
	m2 := m1
	m2["hello"] = "world"

	fmt.Println(m1) // map[hello:world]
	fmt.Println(m2) // map[hello:world]
}
