package main

import (
	"context"
	"errors"
	"fmt"
	"sync"
	"time"
)

/*
Requirements:
 - multiple subscribers per topic
 - every published message must be delivered to all subscribers
 - subscriber processes message and calls Ack()
 - publisher must wait until:
    - all subscribers acked OR
    - context cancelled
 - slow subscriber must not block other subscribers forever
 - thread-safe
 - unsubscribe support
 - no goroutine leaks
 - graceful shutdown
*/

type SubscribersByID map[int]chan Delivery

type Message struct {
	ID   int
	Data string
}

type Delivery struct {
	Message Message
	Ack     func()
}

type Broker struct {
	topicsSubscribers map[string]SubscribersByID
	mu                sync.Mutex
	isClosed          bool
	msgID             int
	subscriberID      int
}

func NewBroker() *Broker {
	return &Broker{
		topicsSubscribers: make(map[string]SubscribersByID),
	}
}

func (b *Broker) Subscribe(
	topic string,
	buffer int,
) (<-chan Delivery, func()) {
	/*
		Requirements:
		- each subscriber has own buffered channel
		- unsubscribe removes subscriber
		- unsubscribe closes channel
		- thread-safe
	*/
	if topic == "" {
		topic = "default"
	}

	if buffer == 0 {
		buffer = 1
	}

	b.mu.Lock()
	if b.isClosed {
		b.mu.Unlock()
		return nil, nil
	}

	deliveryCh := make(chan Delivery, buffer)
	_, exists := b.topicsSubscribers[topic]
	if !exists {
		b.topicsSubscribers[topic] = make(SubscribersByID)
	}
	b.subscriberID++
	subscriberID := b.subscriberID
	b.topicsSubscribers[topic][subscriberID] = deliveryCh
	b.mu.Unlock()

	unsubscribe := func() {
		b.mu.Lock()
		defer b.mu.Unlock()

		topicsSubscribers, ok := b.topicsSubscribers[topic]
		if !ok {
			return
		}

		if _, ok := topicsSubscribers[subscriberID]; !ok {
			return
		}

		delete(topicsSubscribers, subscriberID)
		close(deliveryCh)
	}

	return deliveryCh, unsubscribe
}

func (b *Broker) Publish(
	ctx context.Context,
	topic string,
	msg Message,
) error {
	/*
		Requirements:
		- deliver to all subscribers
		- wait until all acked
		- respect context cancellation
		- thread-safe
	*/
	if topic == "" {
		return errors.New("empty topic")
	}

	if msg.Data == "" {
		return errors.New("empty message")
	}

	b.mu.Lock()
	if b.isClosed {
		b.mu.Unlock()
		return errors.New("broker is closed")
	}

	topicsSubscribers, exists := b.topicsSubscribers[topic]
	if !exists {
		b.mu.Unlock()
		return fmt.Errorf("topic doesn't exist: %s", topic)
	}

	b.msgID++
	messageID := b.msgID

	deliveryChannels := make([]chan Delivery, 0, len(topicsSubscribers))
	for _, ch := range topicsSubscribers {
		deliveryChannels = append(deliveryChannels, ch)
	}

	ackChannelsList := make([]chan struct{}, 0, len(deliveryChannels))
	for _, ch := range deliveryChannels {
		ackCh := make(chan struct{}, 1)
		ackChannelsList = append(ackChannelsList, ackCh)

		var ackOnce sync.Once
		ack := func() {
			ackOnce.Do(func() {
				ackCh <- struct{}{}
			})
		}

		delivery := Delivery{
			Message: Message{
				ID:   messageID,
				Data: msg.Data,
			},
			Ack: ack,
		}

		select {
		case <-ctx.Done():
			b.mu.Unlock()
			return ctx.Err()
		case ch <- delivery:
		}
	}
	b.mu.Unlock()

	for _, ackCh := range ackChannelsList {
		select {
		case <-ctx.Done():
			return ctx.Err()
		case <-ackCh:
		}
	}

	return nil
}

func (b *Broker) Close() {
	/*
		Requirements:
		- close all subscriber channels
		- graceful shutdown
		- no goroutine leaks
	*/
	b.mu.Lock()
	defer b.mu.Unlock()

	if b.isClosed {
		return
	}

	b.isClosed = true
	for topic := range b.topicsSubscribers {
		for subscriberID := range b.topicsSubscribers[topic] {
			close(b.topicsSubscribers[topic][subscriberID])
		}
	}
	b.topicsSubscribers = make(map[string]SubscribersByID)
}

func main() {
	b := NewBroker()

	sub1, _ := b.Subscribe("orders", 10)
	sub2, _ := b.Subscribe("orders", 10)

	go func() {
		for d := range sub1 {
			fmt.Println("sub1 got:", d.Message.Data)

			time.Sleep(1 * time.Second)

			d.Ack()
		}
	}()

	go func() {
		for d := range sub2 {
			fmt.Println("sub2 got:", d.Message.Data)

			time.Sleep(2 * time.Second)

			d.Ack()
		}
	}()

	ctx, cancel := context.WithTimeout(
		context.Background(),
		5*time.Second,
	)
	defer cancel()

	err := b.Publish(ctx, "orders", Message{
		ID:   1,
		Data: "new-order",
	})

	fmt.Println("publish result:", err)

	time.Sleep(3 * time.Second)

	b.Close()
}
