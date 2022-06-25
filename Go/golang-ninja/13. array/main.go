package main

import (
	"errors"
	"fmt"
)

func main() {
	messages := [3]string{"1", "2", "3"}
	fmt.Println(messages)    // [1 2 3]
	//messages[3] = "4" - так не сделаем
	fmt.Println(messages[1]) // 2

	messages[1] = "5"
	fmt.Println(messages) // [1 5 3]

	printMessages(messages)
}

func printMessages(messages [3]string) error {
	if len(messages) == 0 {
		return errors.New("empty array")
	}
	fmt.Println(messages)
	return nil
}
