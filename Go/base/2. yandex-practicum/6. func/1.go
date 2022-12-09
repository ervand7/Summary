package main

import "fmt"

func FindIndex(data string, a rune) (index int, ok bool) {
	for i, letter := range []rune(data) {
		if letter == a {
			return i, true
		}
	}
	return // вернутся значения по умолчанию
}

func main() {
	fmt.Println(FindIndex("Привет", 'т')) // 5 true
	fmt.Println(FindIndex("Привет", '0')) // 0 false
}
