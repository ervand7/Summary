package main

import (
	"fmt"
	"math"
)

type Shape interface {
	Area() float32
}

type Square struct {
	sideLength float32
}

func (s Square) Area() float32 {
	return s.sideLength * s.sideLength
}

type Circle struct {
	radius float32
}

func (c Circle) Area() float32 {
	return c.radius * c.radius * math.Pi
}

// this func receives an interface as arg
func printShapeArea(shape Shape) {
	fmt.Println(shape.Area())
}

func main() {
	square := Square{5}
	circle := Circle{8}

	printShapeArea(square) // 25
	printShapeArea(circle) // 201.06194
}
