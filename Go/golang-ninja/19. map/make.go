package main

import "fmt"

func main() {
	users := make(map[string]int)
	users["Vasya"] = 19
	fmt.Println(users)
}
