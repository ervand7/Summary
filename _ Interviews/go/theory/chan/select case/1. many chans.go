package main

import (
	"fmt"
	"time"
)

/*
Код выведет либо 1, либо 2.

В select мы можем читать сразу из нескольких каналов.
Важно: в операторе select выполняется только один из блоков case.
Если подходят одновременно несколько условий, то вариант выбирается
случайным образом — порядок case не имеет значения. Если вы хотите
постоянно проверять условия оператора, то поместите select в цикл for.
*/

func main() {
	a := make(chan int)
	b := make(chan int)

	go func() {
		a <- 1
	}()
	go func() {
		b <- 2
	}()
	time.Sleep(10 * time.Millisecond)
	select {
	case v := <-a:
		fmt.Print(v)
	case v := <-b:
		fmt.Print(v)
	}
}
