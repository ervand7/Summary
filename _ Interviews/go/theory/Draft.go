package main

import (
	"fmt"
	"sync"
)

type account struct {
	balance int
}

func deposit(acc *account, amount int) {
	acc.balance += amount
}

func main() {
	acc := account{balance: 0}
	var wg sync.WaitGroup

	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go func(n int) {
			deposit(&acc, 1)
			wg.Done()
		}(i)
	}
	wg.Wait()

	fmt.Printf("balance=%d\n", acc.balance)
}
