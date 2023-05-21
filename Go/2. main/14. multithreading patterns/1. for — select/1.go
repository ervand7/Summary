package main

import "fmt"

func fibonacci(ch chan int, quit chan bool) {
	x, y := 0, 1
	for {
		select {
		case ch <- x:
			x, y = y, x+y
		case <-quit:
			fmt.Println("quit")
			return
		}
	}
}

func main() {
	ch := make(chan int)
	quit := make(chan bool)

	go func() {
		for i := 0; i < 10; i++ {
			fmt.Println(<-ch)
		}
		quit <- true
	}()

	fibonacci(ch, quit)
}

/*
Паттерн может использоваться и без блокирующих операций в case.
Вполне корректна следующая конструкция:

for {
    select {
    case <-quit:
        return
    default:
        // выполняем блокирующую операцию здесь
    }
}
*/
