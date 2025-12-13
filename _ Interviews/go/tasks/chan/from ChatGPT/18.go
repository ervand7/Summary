package main

import (
	"fmt"
	"sync"
)

// Requirements:
// multiple producers, multiple consumers
// Push blocks when capacity is full
// Pop blocks when empty
// must NOT use buffered channels as the queue itself
// must use sync.Mutex + sync.Cond or combination of mutex + channels
// must be safe under race detector

// BoundedQueue is a fixed-capacity FIFO queue with blocking Push/Pop.
type BoundedQueue[T any] struct {
	mu       sync.Mutex
	notEmpty *sync.Cond
	notFull  *sync.Cond

	data     []T
	head     int
	tail     int
	size     int
	capacity int
}

func NewBoundedQueue[T any](capacity int) *BoundedQueue[T] {
	if capacity <= 0 {
		panic("capacity must be > 0")
	}

	q := &BoundedQueue[T]{
		data:     make([]T, capacity),
		capacity: capacity,
	}
	q.notEmpty = sync.NewCond(&q.mu)
	q.notFull = sync.NewCond(&q.mu)

	return q
}

// Push blocks if queue is full.
func (q *BoundedQueue[T]) Push(item T) {
	q.mu.Lock()
	defer q.mu.Unlock()

	for q.size == q.capacity {
		q.notFull.Wait()
	}

	q.data[q.tail] = item
	q.tail = (q.tail + 1) % q.capacity
	q.size++

	q.notEmpty.Signal()
}

// Pop blocks if queue is empty.
func (q *BoundedQueue[T]) Pop() T {
	q.mu.Lock()
	defer q.mu.Unlock()

	for q.size == 0 {
		q.notEmpty.Wait()
	}

	item := q.data[q.head]
	q.head = (q.head + 1) % q.capacity
	q.size--

	q.notFull.Signal()

	return item
}

func main() {
	var wg sync.WaitGroup

	q := NewBoundedQueue[int](10)

	// Producers
	for i := 0; i < 100; i++ {
		wg.Add(1)
		go func(v int) {
			defer wg.Done()
			q.Push(v)
		}(i)
	}

	// Consumers
	for i := 0; i < 100; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			val := q.Pop()
			fmt.Println("got:", val)
		}()
	}

	wg.Wait()
	fmt.Println("Done")
}
