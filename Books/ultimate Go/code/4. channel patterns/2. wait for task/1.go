package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

/*
Отличие от `wait for result` в том, что тут наоборот, parent пишет,
а child читает
*/

func main() {
	ch := make(chan string)
	var wg sync.WaitGroup
	wg.Add(1)
	go func() {
		time.Sleep(time.Duration(rand.Intn(500)) * time.Millisecond)
		d := <-ch
		fmt.Println("child : recv'd signal :", d)
		wg.Done()
	}()

	ch <- "data"
	fmt.Println("parent : sent signal")
	wg.Wait()
}
