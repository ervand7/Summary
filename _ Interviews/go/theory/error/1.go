package main

import (
	"log"
)

/*
Мораль: не нужно возвращать какую-то конкретную ошибку. Нужно возвращать
только интерфейс. Тут мы получаем неожиданный результат по этой причине
*/

type customError struct{}

func (c *customError) Error() string {
	return "Find the bug."
}

func fail() ([]byte, *customError) {
	return nil, nil
}

func main() {
	var err error
	if _, err = fail(); err != nil {
		log.Fatal("Why did this fail?")
	}
	log.Println("No Error")
}

// 2023/05/01 15:22:13 Why did this fail?
