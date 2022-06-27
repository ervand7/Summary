package main

import "fmt"

type MySquare struct {
	sideLength float32
}

func (s MySquare) Area() float32 {
	return s.sideLength * s.sideLength
}

func main() {
	square := MySquare{5}
	printInterface(square)   // {sideLength:5}
	printInterface("qwerty") // qwerty
	printInterface(22)       // 22
	printInterface(true)     // true
}

func printInterface(i interface{}) {
	fmt.Printf("%+v\n", i)
}
