package main

import (
	"fmt"
	"math"
	"strings"
)

func main() {
	// создаём экземпляр strings.Builder
	b := strings.Builder{}

	for i := 0; i < 50; i++ {
		// функция fmt.Fprintf принимает аргументом io.Writer
		// благодаря этому можно записывать форматированный вывод
		fmt.Fprintf(&b, "%v", math.NaN())
	}

	b.Write([]byte("... BATMAN!"))
	b.Write([]byte(" Hello, world!"))

	// выводим собранную строку
	fmt.Printf("%s\n", &b) // NaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaN... BATMAN! Hello, world!
}
