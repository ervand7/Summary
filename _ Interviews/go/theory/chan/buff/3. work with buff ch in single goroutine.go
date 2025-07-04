package main

import "fmt"

/*
Мы можем сколько угодно записывать/читать из буф канала находясь в одной
единственной горутине с условием того, что не будем переполнять буфер
*/

func main() {
	ch := make(chan int, 1)
	ch <- 1
	fmt.Println(<-ch)

	ch <- 2
	fmt.Println(<-ch)

	ch <- 3
	fmt.Println(<-ch)
}

/*
1
2
3
*/
