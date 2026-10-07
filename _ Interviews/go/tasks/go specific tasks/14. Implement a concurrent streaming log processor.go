package main

import (
	"errors"
	"fmt"
	"sync"
	"time"
)

/*
Requirements:
 - multiple producers write logs concurrently
 - processor batches logs
 - flush batch when:
   - batch size reached OR
   - flush timeout reached
 - flushes happen asynchronously
 - preserve log order inside batch
 - graceful shutdown flushes remaining logs
 - backpressure support (writers block when overloaded)
 - no goroutine leaks
 - thread-safe
*/

func FlushLogs(batch []string) error {
	fmt.Println("FLUSH:", batch)
	time.Sleep(300 * time.Millisecond)
	return nil
}

var ErrClosed = errors.New("log processor is closed")

type LogProcessor struct {
	batchSize     int
	flushInterval time.Duration
	closed        bool
	queue         chan string
	batches       chan []string
	mu            sync.RWMutex
	wg            sync.WaitGroup
}

func NewLogProcessor(
	batchSize int,
	flushInterval time.Duration,
	queueSize int,
) *LogProcessor {
	if batchSize < 1 {
		batchSize = 1
	}
	if queueSize < 0 {
		queueSize = 0
	}
	if flushInterval <= 0 {
		flushInterval = time.Second
	}

	p := &LogProcessor{
		batchSize:     batchSize,
		flushInterval: flushInterval,
		queue:         make(chan string, queueSize),
		batches:       make(chan []string, 1),
	}

	p.wg.Add(2)
	go p.batchLoop()
	go p.flushLoop()

	return p
}

func (p *LogProcessor) Write(log string) error {
	if log == "" {
		return nil
	}

	p.mu.RLock()
	defer p.mu.RUnlock()

	if p.closed {
		return ErrClosed
	}

	p.queue <- log
	return nil
}

func (p *LogProcessor) Close() error {
	p.mu.Lock()
	if p.closed {
		p.mu.Unlock()
		return ErrClosed
	}
	p.closed = true
	close(p.queue)
	p.mu.Unlock()

	p.wg.Wait()
	return nil
}

func (p *LogProcessor) batchLoop() {
	defer p.wg.Done()
	defer close(p.batches)

	ticker := time.NewTicker(p.flushInterval)
	defer ticker.Stop()

	batch := make([]string, 0, p.batchSize)

	flush := func() {
		if len(batch) == 0 {
			return
		}
		p.batches <- batch
		batch = make([]string, 0, p.batchSize)
		ticker.Reset(p.flushInterval)
	}

	for {
		select {
		case log, ok := <-p.queue:
			if !ok {
				flush()
				return
			}
			batch = append(batch, log)
			if len(batch) == p.batchSize {
				flush()
			}

		case <-ticker.C:
			flush()
		}
	}
}

func (p *LogProcessor) flushLoop() {
	defer p.wg.Done()

	for batch := range p.batches {
		if err := FlushLogs(batch); err != nil {
			fmt.Printf("lush error: %v", err)
		}
	}
}
func main() {
	p := NewLogProcessor(
		3,
		2*time.Second,
		10,
	)

	var wg sync.WaitGroup

	for i := range 20 {
		wg.Add(1)

		go func(i int) {
			defer wg.Done()

			if err := p.Write(fmt.Sprintf("log-%d", i)); err != nil {
				fmt.Println("write error:", err)
			}
		}(i)
	}

	wg.Wait()

	if err := p.Close(); err != nil {
		fmt.Println("close error:", err)
	}
}
