package main

import "fmt"

func main() {
	ch := make(chan int, 11)

	go func() {
		for i := 0; i < 11; i++ {
			ch <- i
		}
		close(ch)
	}()
	for _ = range ch {
		select {
		case i := <-ch:
			fmt.Print(i)
		}
	}
	// 135790

	/*
		for i := 0; i < 11; i++ {
			v := <-ch
			fmt.Print(v)
		}
		// 012345678910
	*/
}
