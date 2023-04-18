package main

import "fmt"

type MSquare struct {
	sideLength float32
}

func (s MSquare) Area() float32 {
	return s.sideLength * s.sideLength
}

func main() {
	square := MSquare{5}
	defineType(square)   // unknown type
	defineType("qwerty") // unknown type
	defineType(22)       // int 22
	defineType(true)     // bool true
}

func defineType(i interface{}) {
	switch value := i.(type) {
	case int:
		fmt.Println("int", value)
	case bool:
		fmt.Println("bool", value)
	default:
		fmt.Println("unknown type")
	}
}