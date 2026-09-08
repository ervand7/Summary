package main

import (
	"context"
	"errors"
	"fmt"
	"sync"
	"time"
)

type Job struct {
	ID      int
	Payload string
}

type Outcome struct {
	JobID int
	Value string
}

func ExecuteJob(ctx context.Context, job Job) (Outcome, error) {
	select {
	case <-time.After(100 * time.Millisecond):
		if job.ID%7 == 0 {
			return Outcome{}, errors.New("job failed")
		}
		return Outcome{
			JobID: job.ID,
			Value: "processed: " + job.Payload,
		}, nil

	case <-ctx.Done():
		return Outcome{}, ctx.Err()
	}
}

func ProcessJobs(ctx context.Context, jobs []Job, workers int, rps int) ([]Outcome, error) {
	if workers <= 0 {
		return nil, errors.New("workers count should be positive")
	}
	if rps <= 0 {
		return nil, errors.New("rps should be positive")
	}

	var (
		wg     sync.WaitGroup
		mu     sync.Mutex
		jobsCh = make(chan Job)
		errs   = make([]error, 0)
		result = make([]Outcome, 0)
	)

	limiter := time.NewTicker(time.Duration(rps))
	defer limiter.Stop()

	for i := 0; i < workers; i++ {
		wg.Add(1)

		go func() {
			defer wg.Done()

			for job := range jobsCh {
				select {
				case <-ctx.Done():
					return
				case <-limiter.C:
				}

				processed, err := ExecuteJob(ctx, job)

				mu.Lock()
				if err != nil {
					errs = append(errs, err)
				} else {
					result = append(result, processed)
				}
				mu.Unlock()
			}
		}()
	}

stopProduce:
	for _, job := range jobs {
		select {
		case <-ctx.Done():
			break stopProduce
		case jobsCh <- job:
		}
	}

	close(jobsCh)
	wg.Wait()

	if ctx.Err() != nil {
		return result, ctx.Err()
	}

	if len(errs) != 0 {
		return result, errors.Join(errs...)
	}

	return result, nil
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
	defer cancel()

	jobs := make([]Job, 30)
	for i := range jobs {
		jobs[i] = Job{ID: i + 1, Payload: fmt.Sprintf("payload-%d", i+1)}
	}

	Outcomes, err := ProcessJobs(ctx, jobs, 5, 10)

	fmt.Println("error:", err)
	fmt.Println("Outcomes:", len(Outcomes))
}
