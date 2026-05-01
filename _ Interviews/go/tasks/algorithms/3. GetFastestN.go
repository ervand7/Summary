package main

import (
	"context"
	"errors"
	"fmt"
	"sync"
	"time"
)

// You have multiple external providers (like APIs or caches).
// Each provider can return a result or an error with some delay.

// 📌 Requirements
// Run all providers concurrently.
// Return first N successful results (order does NOT matter).
// As soon as you collected N successes → cancel everything else.
// If it's impossible to get N successes (too many errors) → return: error

// ⚠️ Edge Cases
// n > len(providers) → error
// n == 0 → return empty slice
// slow providers must not block fast ones
// some providers may:
//  - return error immediately
//  - hang until context is canceled
//  - be very slow

// 🔥 What is being tested
// This is classic senior-level Go:
// fan-out / fan-in
//  - cancellation propagation
//  - partial results
//  - backpressure
//  - correctness under race conditions
//  - resource cleanup

type Provider interface {
	Get(ctx context.Context, key string) (string, error)
}

type Result struct {
	Val string
	Err error
}

var (
	NotEnoughProviders = errors.New("not enough providers")
)

func GetFastestN(ctx context.Context, providers []Provider, key string, n int) ([]string, error) {
	if n == 0 {
		return []string{}, nil
	}

	providersCount := len(providers)
	if n > providersCount {
		return nil, NotEnoughProviders
	}

	ctx, cancel := context.WithCancel(ctx)
	defer cancel()

	var (
		wg      sync.WaitGroup
		results = make(chan Result, providersCount)
	)

	for _, provider := range providers {
		wg.Add(1)

		go func(p Provider) {
			defer wg.Done()

			val, err := p.Get(ctx, key)
			select {
			case results <- Result{Val: val, Err: err}:
			case <-ctx.Done():
				return
			}
		}(provider)
	}

	go func() {
		wg.Wait()
		close(results)
	}()

	var (
		collected = make([]string, 0, n)
		errs      = make([]error, 0)
	)

	for r := range results {
		if r.Err != nil {
			errs = append(errs, r.Err)
			continue
		}

		collected = append(collected, r.Val)

		if len(collected) == n {
			cancel()
			return collected, nil
		}
	}

	return nil, errors.Join(errs...)
}

type mockProvider struct {
	name  string
	value string
	err   error
	delay time.Duration
}

func (m mockProvider) Get(ctx context.Context, key string) (string, error) {
	select {
	case <-time.After(m.delay):
		if m.err != nil {
			return "", fmt.Errorf("%s: %w", m.name, m.err)
		}
		return fmt.Sprintf("%s:%s", m.name, m.value), nil
	case <-ctx.Done():
		return "", ctx.Err()
	}
}

func main() {
	providers := []Provider{
		mockProvider{name: "p1", value: "A", delay: 100 * time.Millisecond},
		mockProvider{name: "p2", err: fmt.Errorf("fail"), delay: 50 * time.Millisecond},
		mockProvider{name: "p3", value: "B", delay: 200 * time.Millisecond},
		mockProvider{name: "p4", value: "C", delay: 300 * time.Millisecond},
		mockProvider{name: "p5", err: fmt.Errorf("fail"), delay: 150 * time.Millisecond},
	}

	ctx, cancel := context.WithTimeout(context.Background(), 500*time.Millisecond)
	defer cancel()

	n := 2

	results, err := GetFastestN(ctx, providers, "key", n)
	if err != nil {
		fmt.Println("error:", err)
		return
	}

	fmt.Println("results:", results)
}
