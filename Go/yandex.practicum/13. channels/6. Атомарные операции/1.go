package main

import (
	"fmt"
	"math/rand"
	"sync/atomic"
	"time"
)

const (
	StateInitial uint32 = iota
	StateAlive
	StateDied

	reconnectDelay = 500 * time.Millisecond
	maxTries       = 3
)

type Connection struct {
	addr  string
	state uint32
}

func NewConnection(addr string) *Connection {
	c := Connection{
		addr:  addr,
		state: StateInitial,
	}
	return &c
}

func (c *Connection) Addr() string {
	return c.addr
}

func (c *Connection) Connect() error {
	err := c.connect()
	if err != nil {
		return fmt.Errorf("error connecting: %w", err)
	}

	atomic.StoreUint32(&c.state, StateAlive)
	return nil
}

func (c *Connection) connect() error {
	// пропустим реализацию
	return nil
}

func (c *Connection) Send(req []byte) ([]byte, error) {
	// заглушка
	time.Sleep(100 * time.Millisecond)

	// с вероятностью 5% отдадим ошибку
	if rand.Intn(100) < 5 {
		return nil, fmt.Errorf("error sending")
	}

	return []byte("response"), nil
}

func (c *Connection) IsAlive() bool {
	return atomic.LoadUint32(&c.state) == StateAlive
}

func (c *Connection) SetDied() {
	if !atomic.CompareAndSwapUint32(&c.state, StateAlive, StateDied) {
		return
	}

	fmt.Printf("connection %s died, reconnecting later\n", c.addr)
	time.AfterFunc(reconnectDelay, c.reconnect)
}

func (c *Connection) reconnect() {
	err := c.connect()
	if err != nil {
		fmt.Printf("error connecting to %s, reconnecting later: %v\n", c.addr, err)
		time.AfterFunc(reconnectDelay, c.reconnect)
		return
	}

	fmt.Printf("connection %s alive again\n", c.addr)
	atomic.StoreUint32(&c.state, StateAlive)
}

type Status struct {
	Addr string
}

type LoadBalancer struct {
	conns   []*Connection
	counter uint32
}

func NewLoadBalancer(conns []*Connection) *LoadBalancer {
	b := LoadBalancer{
		conns: conns,
	}
	return &b
}

func (b *LoadBalancer) Proxy(req []byte) ([]byte, Status, error) {
	try := 0

	for i := 0; i < len(b.conns) && try < maxTries; i++ {
		idx := atomic.AddUint32(&b.counter, 1) % uint32(len(b.conns))
		conn := b.conns[idx]

		if !conn.IsAlive() {
			continue
		}

		resp, err := conn.Send(req)
		try++
		if err != nil {
			conn.SetDied()
			continue
		}

		st := Status{Addr: conn.Addr()}
		return resp, st, err
	}

	return nil, Status{}, fmt.Errorf("no alive connections")
}

func main() {
	addrs := []string{
		"127.0.0.1:8080",
		"127.0.0.1:8081",
		"127.0.0.1:8082",
		"127.0.0.1:8083",
		"127.0.0.1:8084",
		"127.0.0.1:8085",
	}

	conns := make([]*Connection, 0, len(addrs))
	for _, addr := range addrs {
		conns = append(conns, NewConnection(addr))
	}

	lb := NewLoadBalancer(conns)

	for _, conn := range conns {
		err := conn.Connect()
		if err != nil {
			fmt.Printf("connect error: %v\n", err)
			return
		}
	}

	for i := 0; i < 100; i++ {
		go func() {
			_, st, err := lb.Proxy([]byte("request"))
			if err != nil {
				fmt.Printf("proxy error: %v\n", err)
				return
			}

			fmt.Printf("proxy success to %s\n", st.Addr)
		}()

		time.Sleep(50 * time.Millisecond)
	}

	time.Sleep(5 * time.Second)
}
