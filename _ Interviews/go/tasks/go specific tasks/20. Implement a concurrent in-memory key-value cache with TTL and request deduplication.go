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

 - concurrent GetOrLoad
 - if key missing/expired:
    - only one loader per key runs concurrently
    - other goroutines wait for same result
 - cached values expire after TTL
 - background cleanup of expired entries
 - thread-safe
 - support context cancellation while waiting
 - graceful shutdown
 - no goroutine leaks
*/

var ErrCacheIsClosed = errors.New("cache is closed")

type val struct {
	ttl time.Time
	v   string
	err error
}

type Cache struct {
	storage       map[string]val
	loadersPerKey map[string]map[chan val]struct{}
	keysLoading   map[string]struct{}
	closeCh       chan struct{}
	isClosed      bool
	mu            sync.RWMutex
}

func NewCache(cleanupInterval time.Duration) *Cache {
	if cleanupInterval <= 0 {
		cleanupInterval = 1
	}

	cache := &Cache{
		closeCh:       make(chan struct{}),
		storage:       make(map[string]val),
		keysLoading:   make(map[string]struct{}),
		loadersPerKey: make(map[string]map[chan val]struct{}),
	}

	go cache.runCleanUp(cleanupInterval)

	return cache
}

func (c *Cache) GetOrLoad(
	ctx context.Context,
	key string,
	ttl time.Duration,
	loader func(context.Context) (string, error),
) (string, error) {
	/*
		Requirements:
		- return cached value if not expired
		- if load already in progress -> wait for same result
		- only one loader per key concurrently
		- support TTL expiration
		- respect context cancellation
		- thread-safe
	*/
	c.mu.RLock()
	if c.isClosed {
		c.mu.RUnlock()
		return "", ErrCacheIsClosed
	}

	cached, exists := c.storage[key]
	if exists {
		if cached.ttl.After(time.Now()) {
			c.mu.RUnlock()
			return cached.v, cached.err
		}
	}
	c.mu.RUnlock()

	c.mu.Lock()
	_, isLoading := c.keysLoading[key]
	if !isLoading {
		c.keysLoading[key] = struct{}{}

		c.mu.Unlock()
		v, err := loader(ctx)
		c.mu.Lock()

		result := val{
			ttl: time.Now().Add(ttl),
			v:   v,
			err: err,
		}
		c.storage[key] = result
		delete(c.keysLoading, key)

		waitChans := c.loadersPerKey[key]
		delete(c.loadersPerKey, key)
		c.mu.Unlock()

		for waitCh := range waitChans {
			waitCh <- result
			close(waitCh)
		}

		return v, err
	}

	waitCh := make(chan val, 1)
	_, exists = c.loadersPerKey[key]
	if !exists {
		c.loadersPerKey[key] = make(map[chan val]struct{})
	}
	c.loadersPerKey[key][waitCh] = struct{}{}
	c.mu.Unlock()

	for {
		select {
		case <-ctx.Done():
			return "", ctx.Err()
		case <-c.closeCh:
			return "", ErrCacheIsClosed
		case cachedResult, ok := <-waitCh:
			if !ok {
				return "", ErrCacheIsClosed
			}
			c.mu.Lock()
			delete(c.loadersPerKey[key], waitCh)
			if len(c.loadersPerKey[key]) == 0 {
				delete(c.loadersPerKey, key)
			}
			c.mu.Unlock()
			return cachedResult.v, cachedResult.err
		}
	}
}

func (c *Cache) Close() {
	/*
		Requirements:
		- stop background cleanup
		- no goroutine leaks
	*/
	c.mu.Lock()
	defer c.mu.Unlock()
	if c.isClosed {
		return
	}

	c.isClosed = true
	close(c.closeCh)
	c.keysLoading = make(map[string]struct{})
	c.loadersPerKey = make(map[string]map[chan val]struct{})
}

func (c *Cache) runCleanUp(cleanupInterval time.Duration) {
	ticker := time.NewTicker(cleanupInterval)
	defer ticker.Stop()

	for {
		select {
		case <-c.closeCh:
			return

		case <-ticker.C:
			c.mu.Lock()
			if c.isClosed {
				c.mu.Unlock()
				return
			}

			now := time.Now()
			for k, v := range c.storage {
				if v.ttl.Before(now) {
					delete(c.storage, k)
				}
			}

			c.mu.Unlock()
		}
	}
}

func main() {
	cache := NewCache(2 * time.Second)

	loader := func(ctx context.Context) (string, error) {
		fmt.Println("LOADER CALLED")

		select {
		case <-time.After(2 * time.Second):
			return "loaded-value", nil

		case <-ctx.Done():
			return "", ctx.Err()
		}
	}

	var wg sync.WaitGroup

	// only ONE loader should execute
	for i := 0; i < 5; i++ {
		wg.Add(1)

		go func(id int) {
			defer wg.Done()

			res, err := cache.GetOrLoad(
				context.Background(),
				"user:1",
				5*time.Second,
				loader,
			)

			fmt.Println(
				"goroutine",
				id,
				"result:",
				res,
				"err:",
				err,
			)
		}(i)
	}

	wg.Wait()

	fmt.Println("SECOND CALL (should use cache)")

	res, err := cache.GetOrLoad(
		context.Background(),
		"user:1",
		5*time.Second,
		loader,
	)

	fmt.Println("cached result:", res, "err:", err)

	fmt.Println("WAITING TTL EXPIRATION")

	time.Sleep(6 * time.Second)

	fmt.Println("THIRD CALL (loader should execute again)")

	res, err = cache.GetOrLoad(
		context.Background(),
		"user:1",
		5*time.Second,
		loader,
	)

	fmt.Println("after ttl:", res, "err:", err)

	cache.Close()
}
