package main

import "fmt"

func sender(c chan int) {
	c <- 1 // len 1, cap 3
	c <- 2 // len 2, cap 3
	c <- 3 // len 3, cap 3
	c <- 4 // <- горутина заблокируется только тут, при переполнении буффера
	close(c)
}

func main() {
	ch := make(chan int, 3)
	go sender(ch)
	fmt.Printf("len is %v and capacity is %v\n", len(ch), cap(ch))

	// read values from c (blocked here)
	for val := range ch {
		fmt.Printf("len after value '%v' is %v\n", val, len(ch))
	}
}

/*
len is 0 and capacity is 3
len after value '1' is 3
len after value '2' is 2
len after value '3' is 1
len after value '4' is 0
*/
