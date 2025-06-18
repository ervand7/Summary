package main

import "fmt"

/*
Здесь даже WaitGroup не нужен, так как после переполнения буфера
планировщик разбудит горутину squares. И она прочтет все значения
*/

func squares(c chan int) {
	for i := 0; i <= 3; i++ {
		num := <-c
		fmt.Println(num * num)
	}
}

func main() {
	fmt.Println("main() started")
	c := make(chan int, 3)

	go squares(c)

	c <- 1
	c <- 2
	c <- 3
	c <- 4 // blocks here

	fmt.Println("main() stopped")
}

/*
main() started
1
4
9
16
main() stopped
*/
