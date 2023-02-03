package main

import (
	"context"
	"sync"
	"time"

	"golang.org/x/sync/singleflight"
)

type CacheKey string

type Cache interface {
	GetValue(ctx context.Context, key CacheKey) (interface{}, error)
}

// CacheValueProvider предоставляет значения, которые будут закешированы
type CacheValueProvider interface {
	GetValue(ctx context.Context, key CacheKey) (interface{}, time.Time, error)
}

type cache struct {
	valueProvider     CacheValueProvider
	storage           sync.Map
	singleFlightGroup *singleflight.Group
}

var _ Cache = (*cache)(nil)

func (c *cache) GetValue(ctx context.Context, key CacheKey) (interface{}, error) {
	existingValue, ok := c.storage.Load(key)
	if !ok {
		return c.refreshKey(ctx, key)
	}

	typedExistingValue := existingValue.(storedValue)

	now := time.Now()
	if now.After(typedExistingValue.expireAt) {
		return c.refreshKey(ctx, key)
	}

	return typedExistingValue.value, nil
}

type storedValue struct {
	value    interface{}
	expireAt time.Time
}

func (c *cache) refreshKey(
	ctx context.Context, key CacheKey,
) (interface{}, error) {
	value, expireAt, err := c.valueProvider.GetValue(ctx, key)
	if err != nil {
		return nil, err
	}

	result := storedValue{
		value:    value,
		expireAt: expireAt,
	}

	c.storage.Store(key, result)

	return result.value, nil
}

type mockValueProvider struct {
	called bool
}

func (p *mockValueProvider) GetValue(
	ctx context.Context, key CacheKey,
) (interface{}, time.Time, error) {
	if !p.called {
		p.called = true
		time.Sleep(10 * time.Millisecond)
		return 1, time.Now().Add(time.Minute), nil
	}
	panic("already called")
}

func main() {
	c := &cache{
		valueProvider:     &mockValueProvider{},
		storage:           sync.Map{},
		singleFlightGroup: &singleflight.Group{},
	}

	for i := 0; i != 100; i++ {
		go func() {
			_, err := c.GetValue(context.TODO(), "1") // panic: already called
			if err != nil {
				panic(err)
			}
		}()
	}
}
