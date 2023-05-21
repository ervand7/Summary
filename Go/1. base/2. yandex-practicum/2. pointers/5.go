package main

import (
	"bufio"
	"fmt"
	"os"
)

func increment(value *int) {
	// dereferencing
	*value++
}

func main() {
	// Получаем читателя пользовательского ввода
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Interaction counter")

	counter := 0
	for {
		fmt.Print("-> ")
		// Считываем введённую пользователем строку.
		// Программа ждёт, пока пользователь введёт строку
		_, err := reader.ReadString('\n')
		if err != nil {
			panic(err)
		}
		increment(&counter)

		fmt.Printf("User input %d lines\n", counter)
	}
}
