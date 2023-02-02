package main

import "fmt"

type myStruct struct {
	first  string
	second int
}

func main() {
	var data myStruct
	fmt.Println(data)
}
