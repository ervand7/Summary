package main

import "fmt"

func main() {
	workers := 10
	for range workers {
		fmt.Println("Hi")
	}
}
