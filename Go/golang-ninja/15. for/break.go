package main

import "fmt"

func main() {
	counter := 0
	for {
		if counter == 100 {
			break
		}
		counter++
		fmt.Println(counter)
	}
}
