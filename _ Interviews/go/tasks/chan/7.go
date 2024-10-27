package main

import "fmt"

// deadlock will happen because for-range will wait after 3rd iteration
// But if we use close(ch) in the bottom of go func, we will not encounter with deadlock

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
