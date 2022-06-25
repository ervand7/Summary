// Slice - is a wrap on array. Under the hood it stores a ref on the array
package main

import (
	"errors"
	"fmt"
)

func main() {
	messages := []string{"1", "2", "3"}
	printMessages(messages) // [1 5 3]
	fmt.Println(messages)   // [1 5 3]
}

func printMessages(messages []string) error {
	if len(messages) == 0 {
		return errors.New("empty array")
	}
	messages[1] = "5"
	fmt.Println(messages)
	return nil
}
