package main

import (
	"context"
	"fmt"
)

func main() {
	/*
		На выходе получаем новый дочерний контекст и функцию cancel,
		с помощью которой можно отменить этот дочерний контекст и всё его дерево.

		Функцию cancel нужно обязательно выполнить в коде, иначе сборщик мусора
		не удалит созданный дочерний контекст и произойдёт утечка памяти.
		Часто используется конструкция defer cancel(), чтобы отменить
		контекст в конце выполнения функции.
	*/
	ctx, cancel := context.WithCancel(context.Background())
	fmt.Println(ctx) // context.Background.WithCancel
	defer cancel()
}
