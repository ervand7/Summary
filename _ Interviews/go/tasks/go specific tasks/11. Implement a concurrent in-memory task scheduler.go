package main

import (
	"errors"
	"fmt"
	"sync"
	"time"
)

/*
Requirements:
 - tasks execute at specified time
 - multiple workers execute tasks concurrently
 - support task cancellation
 - scheduler must be thread-safe
 - scheduler shutdown must stop accepting new tasks
 - no goroutine leaks
 - graceful shutdown waits for running tasks
*/

type Task struct {
	cancel chan struct{}
}

type Scheduler struct {
	tasks   map[string]*Task
	mu      sync.Mutex
	wg      sync.WaitGroup
	sem     chan struct{}
	stopped bool
}

func NewScheduler(workers int) *Scheduler {
	if workers <= 0 {
		workers = 1
	}

	return &Scheduler{
		tasks: make(map[string]*Task),
		sem:   make(chan struct{}, workers),
	}
}

func (s *Scheduler) Schedule(id string, runAt time.Time, task func()) error {
	if runAt.IsZero() {
		return errors.New("task runAt should not be zero")
	}

	if task == nil {
		return errors.New("task func should not be nil")
	}

	s.mu.Lock()
	if s.stopped {
		s.mu.Unlock()
		return errors.New("scheduler is stopped")
	}

	if _, exists := s.tasks[id]; exists {
		s.mu.Unlock()
		return fmt.Errorf("task with id %s already exists", id)
	}

	t := &Task{cancel: make(chan struct{})}
	s.tasks[id] = t
	s.wg.Add(1)
	s.mu.Unlock()

	go func() {
		defer s.wg.Done()

		timer := time.NewTimer(time.Until(runAt))
		defer timer.Stop()

		select {
		case <-t.cancel:
			return
		case <-timer.C:
		}

		select {
		case <-t.cancel:
			return
		case s.sem <- struct{}{}:
		}
		defer func() { <-s.sem }()

		s.mu.Lock()
		if s.tasks[id] != t {
			s.mu.Unlock()
			return
		}
		delete(s.tasks, id)
		s.mu.Unlock()

		task()
	}()

	return nil
}

func (s *Scheduler) Cancel(id string) {
	s.mu.Lock()
	defer s.mu.Unlock()

	if task, ok := s.tasks[id]; ok {
		close(task.cancel)
		delete(s.tasks, id)
	}
}

func (s *Scheduler) Stop() {
	s.mu.Lock()
	if s.stopped {
		s.mu.Unlock()
		return
	}

	s.stopped = true

	for _, task := range s.tasks {
		close(task.cancel)
	}
	s.tasks = make(map[string]*Task)
	s.mu.Unlock()

	s.wg.Wait()
}

func main() {
	s := NewScheduler(3)

	_ = s.Schedule(
		"task-1",
		time.Now().Add(2*time.Second),
		func() {
			fmt.Println("task-1 executed")
		},
	)

	_ = s.Schedule(
		"task-2",
		time.Now().Add(1*time.Second),
		func() {
			fmt.Println("task-2 executed")
		},
	)

	_ = s.Schedule(
		"task-3",
		time.Now().Add(3*time.Second),
		func() {
			fmt.Println("task-3 executed")
		},
	)

	s.Cancel("task-3")

	time.Sleep(5 * time.Second)

	s.Stop()
}
