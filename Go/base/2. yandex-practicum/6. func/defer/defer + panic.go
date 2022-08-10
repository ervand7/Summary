package main

import (
	"fmt"
)

func PanicingFunc() {
	defer func() {
		// встроенная функция recover останавливает панику и возвращает описание произошедшего
		if r := recover(); r != nil {
			fmt.Println("Panic is caught.", r)
		}
	}()

	panic("Мне здесь совсем ничего не нравится!")
	/*
		встроенная функция panic () вызывает панику у функции.
		в качестве аргумента ей принято передавать причину паники.
		Именно она будет возвращена функцией recover
	*/
}

func main() {
	PanicingFunc() // Panic is caught. Мне здесь совсем ничего не нравится!
}
