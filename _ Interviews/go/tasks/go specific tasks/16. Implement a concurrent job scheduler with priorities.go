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
	jobs     []job
	ids      map[int]struct{}
	sem      chan struct{}
	notify   chan struct{}
	closeCh  chan struct{}
	wg       sync.WaitGroup
}

func NewPriorityScheduler(workers int, queueSize int) *PriorityScheduler {
	if workers <= 0 {
		workers = 1
	}
	if queueSize <= 0 {
		queueSize = 1
	}

	s := &PriorityScheduler{
		jobs:    make([]job, 0, queueSize),
		ids:     make(map[int]struct{}),
		sem:     make(chan struct{}, queueSize),
		notify:  make(chan struct{}, workers),
		closeCh: make(chan struct{}),
	}

	for i := 0; i < workers; i++ {
		s.wg.Add(1)
		go s.worker()
	}

	return s
}

func (s *PriorityScheduler) worker() {
	defer s.wg.Done()

	for {
		s.mu.Lock()

		if len(s.jobs) == 0 {
			if s.isClosed {
				s.mu.Unlock()
				return
			}

			s.mu.Unlock()

			select {
			case <-s.notify:
				continue
			case <-s.closeCh:
				continue
			}
		}

		bestIdx := 0
		for i := 1; i < len(s.jobs); i++ {
			if s.jobs[i].Priority > s.jobs[bestIdx].Priority {
				bestIdx = i
			}
		}

		j := s.jobs[bestIdx]
		s.jobs = append(s.jobs[:bestIdx], s.jobs[bestIdx+1:]...)
		delete(s.ids, j.ID)
		<-s.sem

		s.mu.Unlock()

		j.Execute()
	}
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
	if _, exists := s.ids[j.ID]; exists {
		s.mu.Unlock()
		return errors.New("job already exists")
	}
	s.mu.Unlock()

	select {
	case <-ctx.Done():
		return ctx.Err()
	case <-s.closeCh:
		return ErrPrioritySchedulerIsClosed
	case s.sem <- struct{}{}:
	}

	s.mu.Lock()
	defer s.mu.Unlock()

	if s.isClosed {
		<-s.sem
		return ErrPrioritySchedulerIsClosed
	}

	s.jobs = append(s.jobs, j)
	s.ids[j.ID] = struct{}{}

	select {
	case s.notify <- struct{}{}:
	default:
	}

	return nil
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
