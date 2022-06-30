package main

import "fmt"

func main() {
	fmt.Println(string("Hello"[1]))             // ASCII only
	fmt.Println(string([]rune("Hello, 世界")[1])) // UTF-8
	fmt.Println(string([]rune("Hello, 世界")[8])) // UTF-8
}
/*
e
e
界
 */