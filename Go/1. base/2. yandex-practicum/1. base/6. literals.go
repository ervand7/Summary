package main

import "fmt"

// Любой из этих литералов может быть использован в выражениях
// и даст одно и то же значение.
func main() {
	fmt.Println(1000)
	fmt.Println(1000.0)
	fmt.Println(1_000)          // можно разделять части числа символом '_' для удобства восприятия
	fmt.Println(01750)          // восьмеричное представление, начинается с 0
	fmt.Println(0x3e8)          // шестнадцатеричное представление
	fmt.Println(0b001111101000) // бинарное представление
}