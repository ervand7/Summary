package main

import "fmt"

func main() {
	s := "Привет"
	// ❌ По байтам (может сломать текст):
	for i := 0; i < len(s); i++ {
		fmt.Println(string(s[i]))
	}

	// ✅ По символам:
	for _, r := range s {
		fmt.Println(string(r))
	}
}
