package main

import "fmt"

type someType struct{}

func printfInterface(i interface{}) {
	switch value := i.(type) {
	case string:
		fmt.Printf("string: %s\n", value)
	case int:
		fmt.Printf("int: %d\n", value)
	case bool:
		fmt.Printf("bool: %t\n", value)
	case someType:
		fmt.Printf("someType: %v\n", value)
	case func(int) bool:
		fmt.Println("func(int) bool")
	default:
		fmt.Println("unknown type")
	}
}

func main() {
	printfInterface("Hello") // string: Hello
	printfInterface(1)       // int: 1
	printfInterface(true)    // bool: true
	s := someType{}
	printfInterface(s) // someType: {}
	f := func(in int) bool { return in > 77 }
	printfInterface(f) // func(int) bool
}
