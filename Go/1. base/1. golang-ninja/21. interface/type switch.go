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
	printfInterface(square)   // unknown type
	printfInterface(square)   // unknown type
	printfInterface("qwerty") // unknown type
	printfInterface(22)       // int 22
	printfInterface(true)     // bool true
}

func printfInterface(i interface{}) {
	switch value := i.(type) {
	case int:
		fmt.Println("int", value)
	case bool:
		fmt.Println("bool", value)
	default:
		fmt.Println("unknown type")
	}
}
