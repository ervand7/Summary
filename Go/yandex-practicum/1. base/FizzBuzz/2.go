package main

import "fmt"

func main() {

	for i := 1; i <= 100; i++ {
		found := false

		if i%3 == 0 {
			fmt.Printf("Fizz")
			found = true
		}
		if i%5 == 0 {
			fmt.Printf("Buzz")
			found = true
		}

		if !found {
			fmt.Println(i)
			continue
		}

		fmt.Println()
	}
}
