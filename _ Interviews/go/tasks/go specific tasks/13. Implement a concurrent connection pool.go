package main

import (
	"context"
	"errors"
	"fmt"
	"sync"
	"time"
)

type Connection struct {
	ID int
}

type Pool struct {
	maxSize          int
	connections      chan *Connection
	connectionsCount int
	mu               sync.Mutex
	isClosed         bool
	connectionsMap   map[*Connection]struct{}
	closeCh          chan struct{}
}

func NewPool(maxSize int) *Pool {
	if maxSize <= 0 {
		maxSize = 1
	}

	return &Pool{
		maxSize:        maxSize,
		connections:    make(chan *Connection, maxSize),
		connectionsMap: make(map[*Connection]struct{}),
		closeCh:        make(chan struct{}),
	}
}

func (p *Pool) Acquire(ctx context.Context) (*Connection, error) {
	p.mu.Lock()
	if p.isClosed {
		p.mu.Unlock()
		return nil, errors.New("pool is closed")
	}

	select {
	case conn := <-p.connections:
		p.mu.Unlock()
		return conn, nil
	default:
	}

	if p.connectionsCount < p.maxSize {
		p.connectionsCount++
		id := p.connectionsCount
		conn := &Connection{ID: id}
		p.connectionsMap[conn] = struct{}{}
		p.mu.Unlock()
		return conn, nil
	}
	p.mu.Unlock()

	select {
	case <-ctx.Done():
		return nil, ctx.Err()

	case <-p.closeCh:
		return nil, errors.New("pool is closed")

	case conn, ok := <-p.connections:
		if !ok {
			return nil, errors.New("pool is closed")
		}
		return conn, nil
	}
}

func (p *Pool) Release(conn *Connection) {
	if conn == nil {
		return
	}

	p.mu.Lock()
	_, exists := p.connectionsMap[conn]
	if !exists {
		p.mu.Unlock()
		return
	}

	if p.isClosed {
		delete(p.connectionsMap, conn)
		p.mu.Unlock()
		return
	}
	p.mu.Unlock()

	select {
	case <-p.closeCh:
		return
	case p.connections <- conn:
	}
}

func (p *Pool) Close() {
	p.mu.Lock()
	defer p.mu.Unlock()

	if p.isClosed {
		return
	}

	p.isClosed = true
	p.connectionsMap = make(map[*Connection]struct{})

	close(p.closeCh)
	close(p.connections)
}

func main() {
	pool := NewPool(2)

	for i := 0; i < 5; i++ {
		go func(id int) {
			ctx, cancel := context.WithTimeout(context.Background(), 3*time.Second)
			defer cancel()

			conn, err := pool.Acquire(ctx)
			if err != nil {
				fmt.Println("worker", id, "acquire error:", err)
				return
			}

			fmt.Println("worker", id, "got conn", conn.ID)

			time.Sleep(2 * time.Second)

			pool.Release(conn)

			fmt.Println("worker", id, "released conn", conn.ID)
		}(i)
	}

	time.Sleep(8 * time.Second)

	pool.Close()
}
