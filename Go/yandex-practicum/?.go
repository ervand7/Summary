package main

import "fmt"

type Item struct {
	NoOption   string
	Parameter1 string
	Parameter2 int
}
type option func(*Item)

func NewItem(opts ...option) *Item {
	// инициализируем типовыми значениями
	i := &Item{
		NoOption:   "usual",
		Parameter1: "default",
		Parameter2: 42,
	}
	// применяем опции в том порядке, в котором они были заявлены
	for _, opt := range opts {
		opt(i)
	}
	return i
}
func Option1(option1 string) option {
	return func(i *Item) {
		i.Parameter1 = option1
	}
}
func Option2(option2 int) option {
	return func(i *Item) {
		i.Parameter2 = option2
	}
}
func main() {
	// с параметрами по умолчанию
	item1 := NewItem()
	fmt.Println(item1) // &{usual default 42}

	// с применением одной опции
	item2 := NewItem(Option2(70)) // &{usual default 70}
	fmt.Println(item2)

	// или двух
	item3 := NewItem(Option1("unusual"), Option2(99))
	fmt.Println(item3) // &{usual unusual 99}

	// опции можно заявлять в разном порядке
	item4 := NewItem(Option2(88), Option1("rare"))
	fmt.Println(item4) // &{usual rare 88}
}
