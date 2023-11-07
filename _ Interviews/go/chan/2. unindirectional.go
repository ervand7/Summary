package main

import "fmt"

/*
1) с помощью функции make можно сразу создавать канал нужной направленности
2) каналы `<-chan int` и `chan<- int` являются разными типами данных
*/

func main() {
	roc := make(<-chan int)
	soc := make(chan<- int)

	fmt.Printf("%T\n", roc) // <-chan int
	fmt.Printf("%T\n", soc) // chan<- int
}
