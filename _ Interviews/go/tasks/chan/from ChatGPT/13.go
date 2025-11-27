package main

import (
	"context"
	"fmt"
	"sync"
	"time"
)

// Goal:
// Merge several input channels into one output channel.
// Stop merging when context is done.
// Question:
// Implement merge().

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 200*time.Millisecond)
	defer cancel()

	c1 := producer("A", 50*time.Millisecond)
	c2 := producer("B", 80*time.Millisecond)
	c3 := producer("C", 120*time.Millisecond)

	out := merge(ctx, c1, c2, c3)

	for v := range out {
		fmt.Println("got:", v)
	}
}

func producer(label string, delay time.Duration) <-chan string {
	ch := make(chan string)
	go func() {
		defer close(ch)
		for i := 1; i <= 5; i++ {
			time.Sleep(delay)
			ch <- fmt.Sprintf("%s-%d", label, i)
		}
	}()
	return ch
}

func merge(ctx context.Context, chans ...<-chan string) <-chan string {
	var wg sync.WaitGroup
	out := make(chan string)

	for _, channel := range chans {
		wg.Add(1)

		go func(ch <-chan string) {
			defer wg.Done()

			for {
				select {
				case <-ctx.Done():
					return
				case val, ok := <-ch:
					if !ok {
						return // channel is closed
					}
					select {
					case <-ctx.Done():
						return
					case out <- val:
					}
				}
			}
		}(channel)
	}

	go func() {
		wg.Wait()
		close(out)
	}()

	return out
}
