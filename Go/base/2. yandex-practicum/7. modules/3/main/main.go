package main

import (
	"fmt"
	"mathslice"
)

func main() {

	s := mathslice.Slice{1, 2, 3}
	fmt.Println(s)                                       // [1 2 3]
	fmt.Println("Сумма слайса: ", mathslice.SumSlice(s)) // Сумма слайса:  6

	mathslice.MapSlice(s, func(i mathslice.Element) mathslice.Element {
		return i * 2
	})

	fmt.Println("Слайс, умноженный на два: ", s)         // Слайс, умноженный на два:  [2 4 6]
	fmt.Println("Сумма слайса: ", mathslice.SumSlice(s)) // Сумма слайса:  12
	fmt.Println("Свёртка слайса умножением ",
		mathslice.FoldSlice(s,
			func(x mathslice.Element, y mathslice.Element) mathslice.Element {
				return x * y
			},
			1)) // Свёртка слайса умножением  48

	fmt.Println("Свёртка слайса сложением ",
		mathslice.FoldSlice(s,
			func(x mathslice.Element, y mathslice.Element) mathslice.Element {
				return x + y
			},
			0)) // Свёртка слайса сложением  12
}
