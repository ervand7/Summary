package main

import "fmt"

// len возвращает длину []byte строки

func main() {
	a := "qwerty"
	fmt.Println(len(a))    // 6
	fmt.Println([]byte(a)) // [113 119 101 114 116 121]

	a = "йцукен"
	fmt.Println(len(a))    // 12
	fmt.Println([]byte(a)) // [208 185 209 134 209 131 208 186 208 181 208 189]
}
