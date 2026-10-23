package main

import "sync"

const bufferSize = 10

// Concurrency Constraints
// ·       The PubSub instance will be shared globally.
// ·       Subscribe and Publish will be called concurrently from hundreds of Goroutines.
// ·       You must ensure thread safety (e.g., no race conditions on the subscriber map).
// . Out of Scope:
// ·       You do not need to implement an Unsubscribe method.
// ·       You do not need to implement a Shutdown or Close method.
// ·       Focus strictly on the subscription and publishing logic.

type PubSub struct {
	bufferSize int
	topics     map[string][]chan string
	mu         sync.RWMutex
}

func NewPubSub() *PubSub {
	return &PubSub{
		bufferSize: bufferSize,
		topics:     make(map[string][]chan string),
	}
}

func (ps *PubSub) Subscribe(topic string) <-chan string {
	ch := make(chan string, ps.bufferSize)

	ps.mu.Lock()
	ps.topics[topic] = append(ps.topics[topic], ch)
	ps.mu.Unlock()

	return ch
}

// Publish Broadcasts the message to all subscribers of the topic
func (ps *PubSub) Publish(topic string, msg string) {
	ps.mu.RLock()
	defer ps.mu.RUnlock()

	for _, ch := range ps.topics[topic] {
		select {
		case ch <- msg:
		default:
		}
	}
}
