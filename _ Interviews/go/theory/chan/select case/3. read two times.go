package main

import "fmt"

func main() {
	ch := make(chan int)

	go func() {
		for i := 0; i < 11; i++ {
			ch <- i
		}
		close(ch)
	}()

	for range ch {
		select {
		case i := <-ch:
			fmt.Println(i)
		}
	}
}
