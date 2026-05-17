package main

import (
	"context"
	"errors"
	"fmt"
	"sync"
	"time"
)

var ErrPrioritySchedulerIsClosed = errors.New("priority scheduler is closed")

type job struct {
	ID       int
	Priority int
	Execute  func()
}

type PriorityScheduler struct {
	mu       sync.Mutex
	isClosed bool

	submitCh chan job
	workCh   chan job
	closeCh  chan struct{}

	wg sync.WaitGroup
}

func NewPriorityScheduler(workers int, queueSize int) *PriorityScheduler {
	if workers <= 0 {
		workers = 1
	}
	if queueSize <= 0 {
		queueSize = 1
	}

	s := &PriorityScheduler{
		submitCh: make(chan job, queueSize),
		workCh:   make(chan job),
		closeCh:  make(chan struct{}),
	}

	s.wg.Add(1)
	go s.dispatcher()

	for i := 0; i < workers; i++ {
		s.wg.Add(1)
		go s.worker()
	}

	return s
}

func (s *PriorityScheduler) Submit(ctx context.Context, j job) error {
	if j.Execute == nil {
		return errors.New("job execute func is nil")
	}

	s.mu.Lock()
	if s.isClosed {
		s.mu.Unlock()
		return ErrPrioritySchedulerIsClosed
	}
	s.mu.Unlock()

	select {
	case <-ctx.Done():
		return ctx.Err()
	case <-s.closeCh:
		return ErrPrioritySchedulerIsClosed
	case s.submitCh <- j:
		return nil
	}
}

func (s *PriorityScheduler) Close() {
	s.mu.Lock()
	if s.isClosed {
		s.mu.Unlock()
		return
	}

	s.isClosed = true
	close(s.closeCh)
	s.mu.Unlock()

	s.wg.Wait()
}

func (s *PriorityScheduler) dispatcher() {
	defer s.wg.Done()
	defer close(s.workCh)

	jobs := make([]job, 0)

	for {
		var next job
		var out chan job

		if len(jobs) > 0 {
			bestIdx := 0
			for i := 1; i < len(jobs); i++ {
				if jobs[i].Priority > jobs[bestIdx].Priority {
					bestIdx = i
				}
			}

			next = jobs[bestIdx]
			jobs = append(jobs[:bestIdx], jobs[bestIdx+1:]...)
			out = s.workCh
		}

		select {
		case j := <-s.submitCh:
			jobs = append(jobs, j)

		case out <- next:

		case <-s.closeCh:
			for len(jobs) > 0 {
				bestIdx := 0
				for i := 1; i < len(jobs); i++ {
					if jobs[i].Priority > jobs[bestIdx].Priority {
						bestIdx = i
					}
				}

				next := jobs[bestIdx]
				jobs = append(jobs[:bestIdx], jobs[bestIdx+1:]...)

				s.workCh <- next
			}

			return
		}
	}
}

func (s *PriorityScheduler) worker() {
	defer s.wg.Done()

	for j := range s.workCh {
		j.Execute()
	}
}

func main() {
	s := NewPriorityScheduler(3, 10)

	var wg sync.WaitGroup

	for i := 0; i < 10; i++ {
		wg.Add(1)

		go func(i int) {
			defer wg.Done()

			j := job{
				ID:       i,
				Priority: i % 3,
				Execute: func() {
					fmt.Println("executing job", i, "priority", i%3, "time", time.Now().Format("15:04:05"))
					time.Sleep(500 * time.Millisecond)
				},
			}

			if err := s.Submit(context.Background(), j); err != nil {
				fmt.Println("submit error:", err)
			}
		}(i)
	}

	wg.Wait()
	s.Close()
}
