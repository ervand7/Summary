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
	id          string
	runAt       time.Time
	f           func()
	stopCh      chan struct{}
	wasCanceled bool
	mu          sync.Mutex
	once        sync.Once
}

type Scheduler struct {
	workers int
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
		workers: workers,
		tasks:   make(map[string]*Task),
		sem:     make(chan struct{}, workers),
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

	t := &Task{
		id:     id,
		runAt:  runAt,
		f:      task,
		stopCh: make(chan struct{}),
	}

	s.tasks[id] = t
	s.wg.Add(1)
	s.mu.Unlock()

	go func() {
		defer s.wg.Done()

		timer := time.NewTimer(time.Until(runAt))
		defer timer.Stop()

		select {
		case <-t.stopCh:
			t.mu.Lock()
			t.wasCanceled = true
			t.mu.Unlock()
			return

		case <-timer.C:
		}

		select {
		case <-t.stopCh:
			return
		case s.sem <- struct{}{}:
		}
		defer func() { <-s.sem }()

		t.mu.Lock()
		canceled := t.wasCanceled
		t.mu.Unlock()

		if !canceled {
			t.f()
		}

		s.mu.Lock()
		delete(s.tasks, id)
		s.mu.Unlock()
	}()

	return nil
}

func (s *Scheduler) Cancel(id string) {
	s.mu.Lock()
	task, ok := s.tasks[id]
	if ok {
		delete(s.tasks, id)
	}
	s.mu.Unlock()

	if !ok {
		return
	}

	task.mu.Lock()
	task.wasCanceled = true
	task.mu.Unlock()

	task.once.Do(func() {
		close(task.stopCh)
	})
}

func (s *Scheduler) Stop() {
	s.mu.Lock()
	if s.stopped {
		s.mu.Unlock()
		return
	}

	s.stopped = true

	tasks := make([]*Task, 0, len(s.tasks))
	for _, task := range s.tasks {
		tasks = append(tasks, task)
	}
	s.mu.Unlock()

	for _, task := range tasks {
		task.mu.Lock()
		task.wasCanceled = true
		task.mu.Unlock()

		task.once.Do(func() {
			close(task.stopCh)
		})
	}

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
