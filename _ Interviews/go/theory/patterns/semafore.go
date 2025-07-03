package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	sem := make(chan struct{}, 3) // максимум 3 одновременно

	var wg sync.WaitGroup
	for i := 0; i < 10; i++ {
		wg.Add(1)
		sem <- struct{}{} // блокируем если лимит
		go func(n int) {
			defer wg.Done()
			defer func() { <-sem }() // освобождаем слот
			fmt.Println("Task", n)
			time.Sleep(time.Second)
		}(i)
	}
	wg.Wait()
}
