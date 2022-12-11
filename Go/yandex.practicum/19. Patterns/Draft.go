package main

import (
	"fmt"
	"os"
	"reflect"
)

func main() {
	filename, _ := os.Executable()
	fmt.Println(reflect.TypeOf(filename))
	_, err := os.Create(".txt")
	fmt.Println(err)
}
