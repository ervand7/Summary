package main

import "fmt"

// объявление типа
type MyType int

// объявление метода
func (m MyType) String() string {
	return fmt.Sprintf("MyType: %d", m)
}

func main() {
	var m MyType = 5

	// вызов метода
	s := m.String()
	fmt.Println(s)
}
