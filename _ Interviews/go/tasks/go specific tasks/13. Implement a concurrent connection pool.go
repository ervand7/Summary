package main

import (
	"context"
	"errors"
	"fmt"
	"sync"
	"sync/atomic"
	"time"
)

var ErrPoolClosed = errors.New("pool is closed")

type Connection struct {
	ID int
}

type Pool struct {
	semaphore chan *Connection
	closed    chan struct{}
	once      sync.Once
	nextID    atomic.Int64

	mu    sync.Mutex
	inUse map[*Connection]struct{}
}

func NewPool(maxSize int) *Pool {
	maxSize = max(maxSize, 1)

	p := &Pool{
		semaphore: make(chan *Connection, maxSize),
		closed:    make(chan struct{}),
		inUse:     make(map[*Connection]struct{}, maxSize),
	}
	for range maxSize {
		p.semaphore <- nil
	}

	return p
}

func (p *Pool) Acquire(ctx context.Context) (*Connection, error) {
	if p.isClosed() {
		return nil, ErrPoolClosed
	}

	select {
	case <-ctx.Done():
		return nil, ctx.Err()
	case <-p.closed:
		return nil, ErrPoolClosed
	case conn := <-p.semaphore:
		if conn == nil {
			conn = &Connection{ID: int(p.nextID.Add(1))}
		}
		p.mu.Lock()
		p.inUse[conn] = struct{}{}
		p.mu.Unlock()
		return conn, nil
	}
}

func (p *Pool) Release(conn *Connection) {
	if conn == nil {
		return
	}

	p.mu.Lock()
	_, ok := p.inUse[conn]
	delete(p.inUse, conn)
	p.mu.Unlock()

	if !ok || p.isClosed() {
		return
	}

	// Never blocks: inUse guarantees at most maxSize tokens in circulation.
	p.semaphore <- conn
}

func (p *Pool) Close() {
	p.once.Do(func() { close(p.closed) })
}

func (p *Pool) isClosed() bool {
	select {
	case <-p.closed:
		return true
	default:
		return false
	}
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
