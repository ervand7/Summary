package main

import "fmt"

func Index(st string, a rune) (index int, ok bool) {
	for i, c := range []rune(st) {
		if c == a {
			return i, true
		}
	}
	return // вернутся значения по умолчанию
}

func main() {
	fmt.Println(Index("Привет", 'т')) // 5 true
	fmt.Println(Index("Привет", '0')) // 0 false
}
