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

type LogProcessor struct {
	batchSize     int
	flushInterval time.Duration
	queueSize     int

	mu       sync.Mutex
	isClosed bool

	queue  chan string
	ticker *time.Ticker

	wg      sync.WaitGroup
	flushWG sync.WaitGroup
}

func NewLogProcessor(
	batchSize int,
	flushInterval time.Duration,
	queueSize int,
) *LogProcessor {
	p := &LogProcessor{
		batchSize:     batchSize,
		flushInterval: flushInterval,
		queueSize:     queueSize,
		queue:         make(chan string, queueSize),
		ticker:        time.NewTicker(flushInterval),
	}

	p.wg.Add(1)
	go p.run()

	return p
}

func (p *LogProcessor) Write(log string) error {
	if len(log) == 0 {
		return nil
	}

	p.mu.Lock()
	if p.isClosed {
		p.mu.Unlock()
		return errors.New("processor is closed")
	}

	// Important: keep lock while sending.
	// This prevents Close from closing the channel at the same time.
	p.queue <- log
	p.mu.Unlock()

	return nil
}

func (p *LogProcessor) run() {
	defer p.wg.Done()
	defer p.ticker.Stop()

	batch := make([]string, 0, p.batchSize)

	flush := func() {
		if len(batch) == 0 {
			return
		}

		batchCopy := append([]string(nil), batch...)
		batch = batch[:0]

		p.flushWG.Add(1)
		go func() {
			defer p.flushWG.Done()

			if err := FlushLogs(batchCopy); err != nil {
				fmt.Println("flush error:", err)
			}
		}()
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

		case <-p.ticker.C:
			flush()
		}
	}
}

func (p *LogProcessor) Close() error {
	p.mu.Lock()

	if p.isClosed {
		p.mu.Unlock()
		return errors.New("pool already closed")
	}

	p.isClosed = true
	close(p.queue)

	p.mu.Unlock()

	p.wg.Wait()
	p.flushWG.Wait()

	return nil
}

func main() {
	p := NewLogProcessor(
		3,
		2*time.Second,
		10,
	)

	var wg sync.WaitGroup

	for i := 0; i < 20; i++ {
		wg.Add(1)

		go func(i int) {
			defer wg.Done()

			err := p.Write(fmt.Sprintf("log-%d", i))
			if err != nil {
				fmt.Println("write error:", err)
			}
		}(i)
	}

	wg.Wait()

	if err := p.Close(); err != nil {
		fmt.Println("close error:", err)
	}
}
