package main

/*
Есть фигуры:
type figures int

const(
    square figures = iota // квадрат
    circle // круг
    triangle // равносторонний треугольник
)

Напишите функцию с такой сигнатурой:
func area(figures)(func(float64) float64, bool)

Функция должна возвращать:
 - функцию для вычисления площади фигуры;
 - true, если фигура известна;
 - false, если фигура неизвестна.
Нужно, чтобы её можно было применять так:

ar, ok := area(myFigure)
if !ok {
    fmt.Println("Ошибка")
    return
}
myArea := ar(x)
*/

import (
	"fmt"
	"reflect"
)

type figures int

const (
	square   figures = iota // квадрат
	circle                  // круг
	triangle                // равносторонний треугольник
)

func area(f figures) (func(float64) float64, bool) {
	switch f {
	case square:
		return func(x float64) float64 { return x * x }, true

	case circle:
		return func(x float64) float64 { return 3.142 * x * x }, true

	case triangle:
		return func(x float64) float64 { return 0.433 * x * x }, true

	default:
		return nil, false
	}
}

func main() {
	fmt.Println(square, circle, triangle) // 0 1 2
	result, _ := area(square)
	fmt.Println(reflect.TypeOf(result)) // func(float64) float64
}
