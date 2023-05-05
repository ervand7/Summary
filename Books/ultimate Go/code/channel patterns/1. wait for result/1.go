package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

/*
Смысл: parent goroutine ждет сигнал от child goroutine
*/

func main() {
	ch := make(chan string)
	var wg sync.WaitGroup
	wg.Add(1)
	go func() {
		time.Sleep(time.Duration(rand.Intn(500)) * time.Millisecond)
		ch <- "data"
		fmt.Println("child : sent signal")
		wg.Done()
	}()
	d := <-ch
	fmt.Println("parent : recv'd signal :", d)

	wg.Wait()
}
