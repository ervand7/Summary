package main

import "fmt"

func main() {
	ch := make(chan int)
	go func() {
		ch <- 1
		ch <- 2
		ch <- 3
	}()

	i := 0
	items := make([]int, 3)
	for item := range ch {
		items[i] = item
		i++
	}
	fmt.Println(items)
}
