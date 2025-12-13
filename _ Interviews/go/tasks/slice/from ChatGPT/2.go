package main

import "fmt"

// Потому что у s нулевая вместимость, каждый append создаёт новый массив,
// поэтому s, a, b и c указывают на разные данные и не влияют друг на друга.

func main() {
	s := make([]int, 0)
	a := append(s, 1)
	b := append(s, 2)
	c := append(s, 3)
	fmt.Println(s)
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
}
