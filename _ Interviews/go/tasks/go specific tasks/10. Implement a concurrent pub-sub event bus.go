package main

import (
	"fmt"
	"sync"
	"time"
)

/*
Requirements:
 - multiple subscribers per topic
 - publishers must not block forever
 - each subscriber has its own buffered channel
 - support unsubscribe
 - thread-safe
 - no goroutine leaks
 - closing the bus must close all subscriber channels
*/

type Subscribers map[int64]chan string

type EventBus struct {
	mu     sync.RWMutex
	topics map[string]Subscribers
	closed bool
	nextID int64
}

func NewEventBus() *EventBus {
	return &EventBus{
		topics: make(map[string]Subscribers),
	}
}

func (b *EventBus) Subscribe(topic string, buffer int) (<-chan string, func()) {
	ch := make(chan string, buffer)

	b.mu.Lock()
	defer b.mu.Unlock()

	if b.closed {
		close(ch)
		return ch, func() {}
	}

	b.nextID++
	subscriberID := b.nextID

	if _, ok := b.topics[topic]; !ok {
		b.topics[topic] = make(Subscribers)
	}

	b.topics[topic][subscriberID] = ch

	var once sync.Once

	unsubscribe := func() {
		once.Do(func() {
			b.mu.Lock()
			defer b.mu.Unlock()

			subs, ok := b.topics[topic]
			if !ok {
				return
			}

			subCh, exists := subs[subscriberID]
			if !exists {
				return
			}

			delete(subs, subscriberID)
			close(subCh)

			if len(subs) == 0 {
				delete(b.topics, topic)
			}
		})
	}

	return ch, unsubscribe
}

func (b *EventBus) Publish(topic string, msg string) {
	b.mu.RLock()
	defer b.mu.RUnlock()

	if b.closed {
		return
	}

	subs, ok := b.topics[topic]
	if !ok {
		return
	}

	for _, ch := range subs {
		select {
		case ch <- msg:
		default:
			// Slow subscriber: skip message.
		}
	}
}

func (b *EventBus) Close() {
	b.mu.Lock()
	defer b.mu.Unlock()

	if b.closed {
		return
	}

	b.closed = true

	for topic, subs := range b.topics {
		for id, ch := range subs {
			close(ch)
			delete(subs, id)
		}
		delete(b.topics, topic)
	}
}

func main() {
	bus := NewEventBus()

	sub1, unsub1 := bus.Subscribe("orders", 2)
	sub2, _ := bus.Subscribe("orders", 2)

	go func() {
		for msg := range sub1 {
			fmt.Println("sub1:", msg)
		}
		fmt.Println("sub1 closed")
	}()

	go func() {
		for msg := range sub2 {
			fmt.Println("sub2:", msg)
		}
		fmt.Println("sub2 closed")
	}()

	bus.Publish("orders", "order-1")
	bus.Publish("orders", "order-2")

	time.Sleep(time.Second)

	unsub1()

	bus.Publish("orders", "order-3")

	time.Sleep(time.Second)

	bus.Close()

	time.Sleep(time.Second)
}
