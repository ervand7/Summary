package main

import "fmt"

func CastToAll(objects []interface{}) {
	for _, obj := range objects {
		fmt.Println(obj)
	}
}
func main() {
	s := make([]int, 5)
	fmt.Println(append(s, 2, 6))
}
