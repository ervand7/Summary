package main

import "fmt"

const (
	Black_ = iota
	Gray_
	White
)

// счётчик обнуляется
const (
	Yellow = iota
	Red
	Green = iota // это присваивание не обнулит iota
	Blue
)

func main() {
	fmt.Println(Black_, Gray_, White)     // 0 1 2
	fmt.Println(Yellow, Red, Green, Blue) // 0 1 2 3
}
