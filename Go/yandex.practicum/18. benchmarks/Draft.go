package main

import (
	"fmt"
)

type Int int

func add(summands ...int) int {
	if len(summands) == 0 {
		return 0
	}
	return summands[0] + add(summands[1:]...)
}

func (i Int) incrementByValue() {
	i += 1
}

func (i *Int) incrementByPtr() {
	*i += 1
}

func main() {
	x := Int(5)
	y := &x
	x.incrementByValue()
	y.incrementByValue()
	fmt.Println(x)  // 5
	fmt.Println(*y) // 5

	x.incrementByPtr()
	fmt.Println(x) // 6
	y.incrementByPtr()
	fmt.Println(x) // 7
	(&x).incrementByPtr()
	fmt.Println(x) // 8
}
