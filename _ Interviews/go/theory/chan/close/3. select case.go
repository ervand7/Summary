package main

import (
	"fmt"
	"sync"
	"time"
)

var channel = make(chan struct{})

func worker(wg *sync.WaitGroup, id int) {
	defer wg.Done()

	for {
		select {
		case <-channel:
			fmt.Println("Завершаем", id)
			return
		default:
			fmt.Println(id)
		}
		time.Sleep(50 * time.Millisecond)
	}
}

func main() {
	var wg sync.WaitGroup
	for i := 0; i < 10; i++ {
		wg.Add(1)
		go worker(&wg, i)
	}
	time.Sleep(1 * time.Second)

	close(channel)
	wg.Wait()
}
