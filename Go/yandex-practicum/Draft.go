package main

import "fmt"

func main() {
	var m map[string]string
	fmt.Println(m)
	if m != nil { // если не проверить это условие,
		m["foo"] = "bar" // то здесь можно получить panic
	} else {
		fmt.Println("Hello")
	}
}
