package main

import (
	"fmt"
	"sync"
)

/*
В данном примере Wait() будет ждать вечно, так как никто не будет
записывать в канал и никто не будет закрывать канал.
*/

var ch = make(chan struct{})

func thread(wg *sync.WaitGroup, i int) {
	defer wg.Done()

	for {
		select {
		case <-ch:
			fmt.Println("Завершаем", i)
			return
		default:
			fmt.Println(i)
		}
	}
}

func main() {
	var wg sync.WaitGroup
	for i := 0; i < 10; i++ {
		wg.Add(1)
		go thread(&wg, i)
	}

	wg.Wait()
}
