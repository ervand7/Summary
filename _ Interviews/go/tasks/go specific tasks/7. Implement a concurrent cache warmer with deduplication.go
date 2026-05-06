package main

import (
	"context"
	"errors"
	"fmt"
	"sync"
	"time"
)

type Value struct {
	Key  string
	Data string
}

func FetchValue(ctx context.Context, key string) (Value, error) {
	select {
	case <-time.After(100 * time.Millisecond):
		if key == "bad" {
			return Value{}, errors.New("fetch failed")
		}
		return Value{
			Key:  key,
			Data: "value-for-" + key,
		}, nil

	case <-ctx.Done():
		return Value{}, ctx.Err()
	}
}

func WarmCache(
	ctx context.Context,
	keys []string,
	workers int,
) (map[string]Value, error) {
	if workers <= 0 {
		return nil, errors.New("workers must be positive")
	}

	ctx, cancel := context.WithCancel(ctx)
	defer cancel()

	var (
		mu     sync.Mutex
		wg     sync.WaitGroup
		cache  = make(map[string]Value)
		errs   []error
		keysCh = make(chan string)
		seen   = make(map[string]struct{})
	)

	for i := 0; i < workers; i++ {
		wg.Add(1)

		go func() {
			defer wg.Done()

			for key := range keysCh {
				select {
				case <-ctx.Done():
					return
				default:
				}

				val, err := FetchValue(ctx, key)

				mu.Lock()
				if err != nil {
					errs = append(errs, err)
					cancel()
				} else {
					cache[key] = val
				}
				mu.Unlock()
			}
		}()
	}

produceLoop:
	for _, key := range keys {
		mu.Lock()
		if _, exists := seen[key]; exists {
			mu.Unlock()
			continue
		}
		seen[key] = struct{}{}
		mu.Unlock()

		select {
		case <-ctx.Done():
			break produceLoop
		case keysCh <- key:
		}
	}

	close(keysCh)
	wg.Wait()

	if len(errs) > 0 {
		return cache, errors.Join(errs...)
	}

	if ctx.Err() != nil {
		return cache, ctx.Err()
	}

	return cache, nil
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
	defer cancel()

	keys := []string{
		"user:1",
		"user:2",
		"user:1",
		"order:1",
		"bad",
		"user:2",
		"product:5",
	}

	cache, err := WarmCache(ctx, keys, 3)

	fmt.Println("error:", err)
	fmt.Println("cache size:", len(cache))

	for k, v := range cache {
		fmt.Println(k, v)
	}
}
