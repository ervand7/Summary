package main

import (
	"bufio"
	"fmt"
	"os"
)

func f(value *int) {
	*value++
}

func main() {
	// Получаем читателя пользовательского ввода
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Interaction counter")

	cnt := 0
	for {
		fmt.Print("-> ")
		// Считываем введённую пользователем строку.
		//Программа ждёт, пока пользователь введёт строку
		_, err := reader.ReadString('\n')
		if err != nil {
			panic(err)
		}
		if err != nil {

		}

		f(&cnt)

		fmt.Printf("User input %d lines\n", cnt)
	}
}
