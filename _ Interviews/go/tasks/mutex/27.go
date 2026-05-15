package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var (
		mu sync.Mutex
		wg sync.WaitGroup
	)
	wg.Add(2)

	go func() {
		defer wg.Done()
		mu.Lock()
		time.Sleep(time.Second * 2)
		fmt.Println("A")
		mu.Unlock()
	}()

	go func() {
		defer wg.Done()
		mu.Lock()
		time.Sleep(time.Second * 2)
		fmt.Println("B")
		mu.Unlock()
	}()

	wg.Wait()
}
