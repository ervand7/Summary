package main

import "fmt"

func main() {
	var key interface{}
	key = "1"
	var list []string
	list = append(list, key.(string))
	fmt.Println(list)
}
