package main

import "fmt"

// MyType объявление типа
type MyType int

// объявление метода
func (m MyType) String() string {
	return fmt.Sprintf("MyType: %d", m)
}

func main() {
	// вызов метода
	var m MyType = 5
	fmt.Println(m.String()) // MyType: 5
}
