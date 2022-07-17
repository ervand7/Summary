package main

import (
	"fmt"
)

var Global = 5

// defer тоже зависит от области видимости. Если прописать его в
// глобальной области видимости, то он вызовется при выходе из программы.
// А если его определить в функции, то он вызовется при выходе из функции

func UseGlobal() {
	defer func(checkout int) {
		Global = checkout
	}(Global)
	Global = 42
	fmt.Println(Global)
	// Здесь будет вызвана отложенная функция, которая изменит 42 на 5
}

func main() {
	fmt.Println(Global) // 5
	UseGlobal()         // 42
	fmt.Println(Global) // 5
}
