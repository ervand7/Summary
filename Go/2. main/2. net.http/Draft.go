package main

import (
	"fmt"
	"reflect"
)

func main() {
	a := make(map[string]string)
	a["qwe"] = "asd"
	fmt.Println(reflect.TypeOf(a["asdasdasd"]))
}
