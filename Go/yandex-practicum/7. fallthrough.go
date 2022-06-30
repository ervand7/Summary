package main

import "fmt"

/*
У ключевого слова fallthrough есть особенности:
 - его можно использовать только в последней строке case,
иначе будет ошибка компиляции;
 - оно игнорирует условие следующего по порядку case.
*/
func main() {
	a := -100
	switch {
	case a > 0:
		if a%2 == 0 {
			break
		}
		fmt.Println("Odd positive value received")
	case a < 0:
		fmt.Println("Negative value received")
		fallthrough
	default:
		fmt.Println("Default value handling")
	}
}
