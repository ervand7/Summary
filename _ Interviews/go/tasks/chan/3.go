package main

import (
	"fmt"
	"sync"
)

var balance int

func init() {
	balance = 100
}

func deposit(val int, wg *sync.WaitGroup, ch chan bool) {
	ch <- true
	balance += val
	<-ch
	wg.Done()
}
func main() {
	var wg sync.WaitGroup
	ch := make(chan bool, 1)
	wg.Add(2)
	go deposit(10, &wg, ch)
	go deposit(20, &wg, ch)
	wg.Wait()
	fmt.Println("Balance is: ", balance)
}
