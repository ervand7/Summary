package main

import (
	"fmt"
	"reflect"
)

type MyType struct {
	IntField int
	StrField string
	PtrField *float64
}

func (mt MyType) IsEqual(mt2 MyType) bool {
	return mt == mt2
}

func (mt MyType) IsEqual2(mt2 MyType) bool {
	return reflect.DeepEqual(mt, mt2)
}

func main() {
	floatValue1, floatValue2 := 10.0, 10.0
	a := MyType{IntField: 1, StrField: "str", PtrField: &floatValue1}
	b := MyType{IntField: 1, StrField: "str", PtrField: &floatValue2}

	fmt.Printf("Равенство a и b: %v\n", a.IsEqual(b))  // Равенство a и b: false
	fmt.Printf("Равенство a и b: %v\n", a.IsEqual2(b)) // Равенство a и b: true
}
