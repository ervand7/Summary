package main

import "fmt"

/*
Мораль: если канал закрыт, но в нем есть значения, то мы сможем прочесть
эти значения. Далее после того как они закончатся, мы будем получать
нулевые значения
*/

func main() {
	ch := make(chan int, 5)
	ch <- 1
	ch <- 2
	ch <- 3
	ch <- 4
	ch <- 5

	counter := 0
	for i := 0; i < 10; i++ {
		if counter == 3 {
			close(ch)
		}
		fmt.Println(<-ch)
		counter++
	}
}

/*
1
2
3
4
5
0
0
0
0
0
*/
