package main

import (
	"fmt"
	"reflect"
)

func PrintType(i interface{}) {
	fmt.Println("Type:", reflect.TypeOf(i))
	fmt.Println("Value:", reflect.ValueOf(i))
}
func main() {
	PrintType(6)
}
