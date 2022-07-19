package main

import "fmt"

// Наличие методов по указателю не обязывает вас
// создавать его экземпляры через указатель:

type SomeType struct {
	value int
}

func (t *SomeType) SetValue(v int) {
	t.value = v
}

func (t SomeType) String() string {
	return fmt.Sprintf("Value: %d", t.value)
}

func main() {
	t := SomeType{}
	// или
	//t := &SomeType{}

	t.SetValue(100)
	fmt.Println(t) // Value: 100
}
