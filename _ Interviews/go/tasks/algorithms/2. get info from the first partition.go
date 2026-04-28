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

// GetFirst1 first option of implementation
func (s Service) GetFirst1(ctx context.Context, key string) (string, error) {
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

			resultCh <- result{
				value: value,
				err:   err,
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

// GetFirst2 second option of implementation
func (s Service) GetFirst2(ctx context.Context, key string) (string, error) {
	if len(s.partitions) == 0 {
		return "", errors.New("no partitions")
	}

	ctx, cancel := context.WithCancel(ctx)
	defer cancel()

	resultCh := make(chan string, 1)
	errCh := make(chan error, len(s.partitions))

	var wg sync.WaitGroup

	for _, partition := range s.partitions {
		wg.Add(1)

		go func(p Rediser) {
			defer wg.Done()

			value, err := p.Get(ctx, key)
			if err != nil {
				errCh <- err
				return
			}

			select {
			case resultCh <- value:
				cancel()
			case <-ctx.Done():
			}
		}(partition)
	}

	go func() {
		wg.Wait()
		close(resultCh)
		close(errCh)
	}()

	select {
	case value, ok := <-resultCh:
		if ok {
			return value, nil
		}

		var errs []error
		for err := range errCh {
			errs = append(errs, err)
		}

		return "", errors.Join(errs...)

	case <-ctx.Done():
		return "", ctx.Err()
	}
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

	result, err := s.GetFirst1(ctx, "key")

	if err != nil {
		fmt.Println("error:", err)
		return
	}

	fmt.Println("result:", result)
}
