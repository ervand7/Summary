package main

import "fmt"

/*
И с помощью for-range мы можем прочесть все значения из закрытого канала
*/

func main() {
	ch := make(chan int, 5)
	ch <- 1
	ch <- 2
	ch <- 3
	ch <- 4
	ch <- 5
	close(ch)

	for value := range ch {
		fmt.Println(value)
	}
}

/*
1
2
3
4
5
*/
