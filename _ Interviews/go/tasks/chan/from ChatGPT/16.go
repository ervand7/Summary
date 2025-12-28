package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	const workers = 5
	b := NewBarrier(workers)

	var wg sync.WaitGroup
	wg.Add(workers)

	for i := 0; i < workers; i++ {
		go func(id int) {
			defer wg.Done()

			fmt.Println("worker", id, "reached barrier 1")
			b.Wait()
			fmt.Println("worker", id, "passed barrier 1")

			fmt.Println("worker", id, "reached barrier 2")
			b.Wait()
			fmt.Println("worker", id, "passed barrier 2")
		}(i)
	}

	wg.Wait()
}

type Barrier struct {
	n       int
	arrive  chan struct{}
	release chan struct{}
}

func NewBarrier(n int) *Barrier {
	return &Barrier{
		n:       n,
		arrive:  make(chan struct{}, n),
		release: make(chan struct{}, n),
	}
}

func (b *Barrier) Wait() {
	time.Sleep(time.Second)

	// Each goroutine signals arrival
	b.arrive <- struct{}{}

	// Last goroutine releases all
	if len(b.arrive) == b.n {
		// Fill release channel with n tokens
		for i := 0; i < b.n; i++ {
			b.release <- struct{}{}
		}
		// Reset arrival channel for next barrier use
		b.arrive = make(chan struct{}, b.n)
	}

	// Each goroutine waits for a release token
	<-b.release
}
