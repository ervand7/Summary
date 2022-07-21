package main

import (
	"fmt"
	"reflect"
)

func main() {
	var varBool *bool
	fmt.Println(reflect.ValueOf(varBool).Kind()) // ptr  указатель
	fmt.Println(reflect.ValueOf(varBool).Type()) // *bool указатель на bool

	var varFloat float32
	fmt.Println(reflect.ValueOf(varFloat).Kind()) // float32
	fmt.Println(reflect.ValueOf(varFloat).Type()) // float32

	var varMap map[string]int
	fmt.Println(reflect.ValueOf(varMap).Kind()) // map
	fmt.Println(reflect.ValueOf(varMap).Type()) // map[string]int

	varStruct := struct{ Value int }{}
	fmt.Println(reflect.ValueOf(varStruct).Kind()) // struct
	fmt.Println(reflect.ValueOf(varStruct).Type()) // struct { Value int }
}
