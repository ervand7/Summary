package main

import (
	"context"
	"errors"
	"fmt"
	"sync"
	"time"
)

// mock implementation
type mockRedis struct {
	name  string
	value string
	err   error
	delay time.Duration
}

func (m mockRedis) Get(_ context.Context, _ string) (string, error) {
	time.Sleep(m.delay)
	if m.err != nil {
		return "", m.err
	}
	return m.value, nil
}

type Rediser interface {
	Get(ctx context.Context, key string) (string, error)
}

type Service struct {
	partitions []Rediser
}

// GetFirst first option of implementation
func (s Service) GetFirst(ctx context.Context, key string) (string, error) {
	if len(s.partitions) == 0 {
		return "", errors.New("no partitions")
	}

	ctx, cancel := context.WithCancel(ctx)
	defer cancel()

	type result struct {
		value string
		err   error
	}

	resultCh := make(chan result, len(s.partitions))

	var wg sync.WaitGroup

	for _, partition := range s.partitions {
		wg.Add(1)

		go func(p Rediser) {
			defer wg.Done()

			value, err := p.Get(ctx, key)

			select {
			case resultCh <- result{value: value, err: err}:
			case <-ctx.Done():
			}
		}(partition)
	}

	go func() {
		wg.Wait()
		close(resultCh)
	}()

	var errs []error

	for res := range resultCh {
		if res.err == nil {
			cancel()
			return res.value, nil
		}

		errs = append(errs, res.err)
	}

	return "", errors.Join(errs...)
}

func main() {
	s := Service{
		partitions: []Rediser{
			mockRedis{name: "p1", err: fmt.Errorf("fail"), delay: 200 * time.Millisecond},
			mockRedis{name: "p2", value: "SUCCESS", delay: 100 * time.Millisecond},
			mockRedis{name: "p3", err: fmt.Errorf("fail"), delay: 300 * time.Millisecond},
		},
	}

	ctx, cancel := context.WithTimeout(context.Background(), 1*time.Second)
	defer cancel()

	result, err := s.GetFirst(ctx, "key")

	if err != nil {
		fmt.Println("error:", err)
		return
	}

	fmt.Println("result:", result)
}
