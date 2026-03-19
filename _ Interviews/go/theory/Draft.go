package main

import "fmt"

func main() {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Hello")
		}

	}()

	panic("boom")
}
