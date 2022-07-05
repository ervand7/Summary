package main

import "fmt"

type figures int

const (
	square   figures = iota // квадрат
	circle                  // круг
	triangle                // равносторонний треугольник
)

func main() {
	fmt.Println(square, circle, triangle)
}
