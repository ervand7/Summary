package main

import "fmt"

type Ivan struct {
	age    int
	weight int
}

func NewIvan() *Ivan {
	return &Ivan{
		age:    20,
		weight: 74,
	}
}

func main() {
	first := NewIvan()
	second := NewIvan()
	fmt.Println(&first)  // 0x1400000e028
	fmt.Println(&second) // 0x1400000e030
}
