package main

import (
	"sync"
	"sync/atomic"
)

type Connection struct{}

type LoadBalancer interface {
	NextConn() *Connection
}

type LoadBalancerChan struct {
	conns []*Connection
	ch    chan *Connection
	stop  chan struct{}
}

func NewLoadBalancerChan(conns []*Connection) *LoadBalancerChan {
	return &LoadBalancerChan{
		conns: conns,
		ch:    make(chan *Connection),
		stop:  make(chan struct{}),
	}
}

func (b *LoadBalancerChan) Init() {
	go b.worker()
}

func (b *LoadBalancerChan) Close() {
	b.stop <- struct{}{}
}

func (b *LoadBalancerChan) worker() {
	for i := 0; ; {
		select {
		case b.ch <- b.conns[i]:
			i++
			if i == len(b.conns) {
				i = 0
			}

		case <-b.stop:
			return
		}
	}
}

func (b *LoadBalancerChan) NextConn() *Connection {
	return <-b.ch
}

type LoadBalancerAtomic struct {
	conns   []*Connection
	counter uint32
}

func NewLoadBalancerAtomic(conns []*Connection) *LoadBalancerAtomic {
	return &LoadBalancerAtomic{conns: conns}
}

func (b *LoadBalancerAtomic) NextConn() *Connection {
	i := atomic.AddUint32(&b.counter, 1) % uint32(len(b.conns))
	return b.conns[i]
}

type LoadBalancerMutex struct {
	conns   []*Connection
	counter int
	mu      sync.Mutex
}

func NewLoadBalancerMutex(conns []*Connection) *LoadBalancerMutex {
	return &LoadBalancerMutex{conns: conns}
}

func (b *LoadBalancerMutex) NextConn() *Connection {
	b.mu.Lock()
	defer b.mu.Unlock()
	b.counter = (b.counter + 1) % len(b.conns)
	return b.conns[b.counter]
}
