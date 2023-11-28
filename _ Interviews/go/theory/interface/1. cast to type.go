package main

import "fmt"

type myType struct{}

func printSomeInterface(i interface{}) {
	if val, ok := i.(string); ok {
		fmt.Printf("string: %s\n", val)
	} else if val, ok := i.(int); ok {
		fmt.Printf("int: %d\n", val)
	} else if val, ok := i.(bool); ok {
		fmt.Printf("bool: %t\n", val)
	} else if val, ok := i.(myType); ok {
		fmt.Printf("myType: %v\n", val)
	} else if _, ok := i.(func(int) bool); ok {
		fmt.Println("func(int) bool")
	}
}

func main() {
	printSomeInterface("Hello") // string: Hello
	printSomeInterface(1)       // int: 1
	printSomeInterface(true)    // bool: true
	s := myType{}
	printSomeInterface(s) // myType: {}
	f := func(in int) bool { return in > 77 }
	printSomeInterface(f) // func(int) bool
}
