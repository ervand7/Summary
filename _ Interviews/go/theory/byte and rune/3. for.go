package main

import "fmt"

func main() {
	s := "Привет"
	for i := 0; i < len([]rune(s)); i++ {
		fmt.Println(string([]rune(s)[i]))
	}

	// ✅ По символам:
	for _, r := range s {
		fmt.Println(string(r))
	}

	fmt.Println(string([]rune(s)[2]))
}
