package main

import (
	"fmt"
	"sync"
)

type Bank struct {
	balance int
	mu      sync.Mutex
}

func (b *Bank) Deposit(v int) {
	b.mu.Lock()
	defer b.mu.Unlock()
	b.balance += v
}

func (b *Bank) Withdraw(v int) bool {
	b.mu.Lock()
	defer b.mu.Unlock()
	if b.balance < v {
		return false
	}
	b.balance -= v
	return true
}

func main() {
	bank := &Bank{balance: 100}
	var wg sync.WaitGroup

	for i := 0; i < 5; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			bank.Withdraw(30)
		}()
	}

	wg.Wait()
	fmt.Println(bank.balance)
}
