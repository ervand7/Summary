package main

import "fmt"

func main() {
	var data *byte
	var in interface{}

	fmt.Println(data, data == nil)
	fmt.Println(in, in == nil)

	in = data // here (type = *byte, value = nil)
	fmt.Println(in, in == nil)
}
