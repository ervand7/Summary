package main

import (
	"fmt"
	"reflect"
)

func main() {
	// The types of arrays will be different depends on array size
	var a [4]int
	fmt.Println(reflect.TypeOf(a)) // [4]int

	var b [5]int
	fmt.Println(reflect.TypeOf(b)) // [5]int
}
