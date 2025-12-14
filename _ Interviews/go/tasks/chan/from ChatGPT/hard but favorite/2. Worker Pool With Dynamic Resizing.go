package main

import (
	"fmt"
	"sync"
	"time"
)

// Behavior:
// - Starts with minWorkers
// - If queued tasks > threshold, pool can spawn up to maxWorkers
// - If workers are idle for longer than idleTimeout, they exit down to minWorkers
// - Stop() waits for all tasks to finish and all workers to exit

type Task func() error

type WorkerPool struct {
	minWorkers  int
	maxWorkers  int
	idleTimeout time.Duration

	tasks chan Task

	mu           sync.Mutex
	workersCount int
	stopping     bool

	wg sync.WaitGroup // waits for workers
}

func NewWorkerPool(minWorkers, maxWorkers int) *WorkerPool {
	if minWorkers <= 0 || maxWorkers < minWorkers {
		panic("invalid workers config")
	}

	p := &WorkerPool{
		minWorkers:  minWorkers,
		maxWorkers:  maxWorkers,
		idleTimeout: 2 * time.Second,
		// buffered queue; capacity is arbitrary, but related to maxWorkers
		tasks: make(chan Task, maxWorkers*4),
	}

	// start with minWorkers
	p.mu.Lock()
	for i := 0; i < minWorkers; i++ {
		p.startWorkerLocked()
	}
	p.mu.Unlock()

	return p
}

func (p *WorkerPool) Submit(t Task) {
	// simple autoscaling on submit: if queue is longer than workers, add worker
	p.mu.Lock()
	if !p.stopping {
		queueLen := len(p.tasks)
		if queueLen >= p.workersCount && p.workersCount < p.maxWorkers {
			p.startWorkerLocked()
		}
	}
	p.mu.Unlock()

	p.tasks <- t
}

func (p *WorkerPool) Stop() {
	p.mu.Lock()
	if p.stopping {
		p.mu.Unlock()
		return
	}
	p.stopping = true
	close(p.tasks)
	p.mu.Unlock()

	p.wg.Wait()
}

func (p *WorkerPool) startWorkerLocked() {
	p.workersCount++
	p.wg.Add(1)
	go p.worker()
}

func (p *WorkerPool) worker() {
	defer p.wg.Done()

	for {
		select {
		case task, ok := <-p.tasks:
			if !ok {
				// pool is stopping, adjust worker count and exit
				p.mu.Lock()
				p.workersCount--
				p.mu.Unlock()
				return
			}

			// execute task
			_ = task()

		case <-time.After(p.idleTimeout):
			// idle too long: try to scale down
			p.mu.Lock()
			if p.stopping {
				p.workersCount--
				p.mu.Unlock()
				return
			}

			if p.workersCount > p.minWorkers && len(p.tasks) == 0 {
				p.workersCount--
				p.mu.Unlock()
				return
			}

			p.mu.Unlock()
		}
	}
}

// Example usage
func main() {
	minWorkers, maxWorkers := 2, 8
	pool := NewWorkerPool(minWorkers, maxWorkers)

	for i := 0; i < 20; i++ {
		i := i
		pool.Submit(func() error {
			time.Sleep(500 * time.Millisecond)
			fmt.Printf("processed task %d\n", i)
			return nil
		})
	}

	// give some time for autoscaling / idling
	time.Sleep(5 * time.Second)

	pool.Stop()
	fmt.Println("pool stopped gracefully")
}
