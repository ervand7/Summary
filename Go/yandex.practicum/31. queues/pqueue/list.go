package pqueue

import (
	"sync"

	"github.com/tmvrus/pqueue/model"
)

type Queue interface {
	Push(job model.Executable, p uint8)
	Pull() model.Executable
}

type PQueue struct {
	lock  *sync.Mutex
	queue *node
}

type node struct {
	priority uint8
	job      model.Executable
	next     *node
	prev     *node
}

func NewPQueue() Queue {
	return &PQueue{
		lock:  &sync.Mutex{},
		queue: nil,
	}
}

func (q *PQueue) Push(job model.Executable, p uint8) {
	n := &node{
		job:      job,
		priority: p,
	}
	q.push(n)
}

func (q *PQueue) push(n *node) {
	q.lock.Lock()
	defer q.lock.Unlock()

	if q.queue == nil {
		q.queue = n
		return
	}
	q.queue.prev = n
	n.next = q.queue
	q.queue = n
}

func (q *PQueue) Pull() model.Executable {
	q.lock.Lock()
	defer q.lock.Unlock()

	if q.queue == nil {
		return nil
	}

	max := q.queue
	next := max.next
	for next != nil {
		// priority handling
		if next.priority > max.priority {
			max = max.next
		}
		next = next.next
	}

	// remove job from queue
	if max.next == nil && max.prev == nil { // one element
		q.queue = nil
	} else if max.next == nil { // last element
		max.prev.next = nil
	} else if max.prev == nil { // first element
		q.queue = max.next
		q.queue.prev = nil
	} else { // middle element
		max.prev.next = max.next
		max.next.prev = max.prev
	}

	return max.job
}
