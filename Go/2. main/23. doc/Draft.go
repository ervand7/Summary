package main

import "fmt"

func main() {
	hashTable := make(map[string]string)
	hashTable["qwe"] = "asd"
	fmt.Println()
	delete(hashTable, "sdfsdf")
	fmt.Println()
}
