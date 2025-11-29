package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	fmt.Println("Start")

	var ch = make(chan int)
	var wg sync.WaitGroup

	wg.Add(1)

	go func() {
		defer wg.Done()
		ch <- 333
		fmt.Println("111")
		time.Sleep(time.Second)
		fmt.Println("222")
		close(ch)
	}()

	for val := range ch {
		fmt.Println(val)
	}

	wg.Wait()
	fmt.Println("Finish")
}
