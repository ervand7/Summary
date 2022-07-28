package main

import (
	"fmt"
)

type Shape_ interface {
	ShapeWithArea
	ShapeWithPerimeter
}

type ShapeWithArea interface {
	Area() float32
}

type ShapeWithPerimeter interface {
	Perimeter() float32
}

type Square_ struct {
	sideLength float32
}

func (s Square_) Area() float32 {
	return s.sideLength * s.sideLength
}

func (s Square_) Perimeter() float32 {
	return s.sideLength * 4
}

func printShapeArea_(shape Shape_) {
	fmt.Println(shape.Area())      // 25
	fmt.Println(shape.Perimeter()) // 20
}

func main() {
	square := Square_{5}
	printShapeArea_(square)
}
