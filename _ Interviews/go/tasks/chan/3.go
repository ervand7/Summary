package main

import (
	"fmt"
	"sync"
)

/*
Если канал будет не буферизированным, то словим deadlock.
Можно читать из буферизированного канала и когда он не переполнен.
*/

var balance int

func init() {
	balance = 100
}

func deposit(val int, wg *sync.WaitGroup, ch chan bool) {
	ch <- true // получили что-то в канал
	balance += val
	<-ch // тут же и прочли
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

// Balance is:  130
