package main

import (
	"context"
	"fmt"
	"sync"
	"sync/atomic"
	"time"
)

// Implement an in-memory event processor in Go.

type Evnt struct {
	ID string
}

// - submitted count
// - processed count
// - dropped count
// - current queue size
type Stats struct {
	submitted        int
	processed        int
	dropped          int
	currentQueueSize int
}

type statsInner struct {
	submitted        atomic.Int64
	processed        atomic.Int64
	dropped          atomic.Int64
	currentQueueSize atomic.Int64
}

type InMemoryProcessor struct {
	isClosed  bool
	isStarted bool
	mu        sync.RWMutex
	wg        sync.WaitGroup
	events    chan Evnt
	stats     statsInner
}

func NewInMemoryProcessor(capacity int) *InMemoryProcessor {
	return &InMemoryProcessor{
		events: make(chan Evnt, capacity),
	}
}

// Non-blocking.
// Sends event to a buffered channel.
// Returns false if the queue is full or processor is stopped.
func (p *InMemoryProcessor) Submit(event Evnt) bool {
	p.mu.RLock()
	defer p.mu.RUnlock()

	if p.isClosed {
		p.stats.dropped.Add(1)
		return false
	}

	select {
	case p.events <- event:
		p.stats.submitted.Add(1)
		p.stats.currentQueueSize.Add(1)
		return true
	default:
		p.stats.dropped.Add(1)
		return false
	}
}

// Starts N worker goroutines.
// Workers process events concurrently.
// Must stop gracefully when context is canceled.
func (p *InMemoryProcessor) Start(ctx context.Context, workers int) {
	p.mu.Lock()
	if p.isStarted || p.isClosed {
		p.mu.Unlock()
		return
	}

	p.isStarted = true
	p.mu.Unlock()

	go func() {
		<-ctx.Done()
		p.Stop()
	}()

	for i := 0; i < workers; i++ {
		p.wg.Add(1)

		go func() {
			defer p.wg.Done()

			for e := range p.events {
				p.stats.currentQueueSize.Add(-1)
				time.Sleep(time.Second)
				fmt.Printf("event %s processed\n", e.ID)
				p.stats.processed.Add(1)
			}
		}()
	}
}

// Stops accepting new events.
// Waits until all queued events are processed.
// Must be safe to call multiple times.
func (p *InMemoryProcessor) Stop() {
	p.mu.Lock()
	if p.isClosed {
		p.mu.Unlock()
		return
	}

	p.isClosed = true
	close(p.events)
	p.mu.Unlock()

	p.wg.Wait()
}

// Returns:
//   - submitted count
//   - processed count
//   - dropped count
//   - current queue size
//
// Must be thread-safe.
func (p *InMemoryProcessor) Stats() Stats {
	return Stats{
		submitted:        int(p.stats.submitted.Load()),
		processed:        int(p.stats.processed.Load()),
		dropped:          int(p.stats.dropped.Load()),
		currentQueueSize: int(p.stats.currentQueueSize.Load()),
	}
}

func main() {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	processor := NewInMemoryProcessor(10)

	// start 4 workers
	processor.Start(ctx, 4)

	var wg sync.WaitGroup

	// simulate concurrent producers
	for producerID := 0; producerID < 5; producerID++ {
		wg.Add(1)

		go func(id int) {
			defer wg.Done()

			for i := 0; i < 20; i++ {
				ok := processor.Submit(Evnt{
					ID: fmt.Sprintf("producer-%d-event-%d", id, i),
				})

				if !ok {
					fmt.Println("dropped:", id, i)
				}

				time.Sleep(50 * time.Millisecond)
			}
		}(producerID)
	}

	wg.Wait()

	// let workers finish processing
	time.Sleep(3 * time.Second)

	processor.Stop()

	fmt.Printf("stats: %+v\n", processor.Stats())
}
