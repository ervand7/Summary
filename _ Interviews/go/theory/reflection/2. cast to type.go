package main

import "fmt"

type Some struct {
	sideLength float32
}

func (s Some) Area() float32 {
	return s.sideLength * s.sideLength
}

func main() {
	square := Some{5}
	printSomeInterface(square)   // interface is not string
	printSomeInterface("qwerty") // 6
	printSomeInterface(22)       // interface is not string
	printSomeInterface(true)     // interface is not string
}

func printSomeInterface(i interface{}) {
	str, ok := i.(string)
	if !ok {
		fmt.Println("interface is not string")
	} else {
		fmt.Println(len(str))
	}
}
