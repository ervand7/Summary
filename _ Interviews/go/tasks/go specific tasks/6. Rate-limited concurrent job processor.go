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

type Resultat struct {
	JobID int
	Value string
}

func ExecuteJob(ctx context.Context, job Job) (Resultat, error) {
	select {
	case <-time.After(100 * time.Millisecond):
		if job.ID%7 == 0 {
			return Resultat{}, errors.New("job failed")
		}
		return Resultat{
			JobID: job.ID,
			Value: "processed: " + job.Payload,
		}, nil

	case <-ctx.Done():
		return Resultat{}, ctx.Err()
	}
}

func ProcessJobs(ctx context.Context, jobs []Job, workers int, rps int) ([]Resultat, error) {
	if workers <= 0 {
		return nil, errors.New("workers must be positive")
	}
	if rps <= 0 {
		return nil, errors.New("rps must be positive")
	}

	jobsCh := make(chan Job)

	var (
		wg      sync.WaitGroup
		mu      sync.Mutex
		results []Resultat
		errs    []error
	)

	limiter := time.NewTicker(time.Second / time.Duration(rps))
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

				res, err := ExecuteJob(ctx, job)

				mu.Lock()
				if err != nil {
					errs = append(errs, err)
				} else {
					results = append(results, res)
				}
				mu.Unlock()
			}
		}()
	}

producerLoop:
	for _, job := range jobs {
		select {
		case <-ctx.Done():
			break producerLoop
		case jobsCh <- job:
		}
	}

	close(jobsCh)
	wg.Wait()

	if ctx.Err() != nil {
		return results, ctx.Err()
	}

	if len(errs) > 0 {
		return results, errs[0]
	}

	return results, nil
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
	defer cancel()

	jobs := make([]Job, 30)
	for i := range jobs {
		jobs[i] = Job{ID: i + 1, Payload: fmt.Sprintf("payload-%d", i+1)}
	}

	Resultats, err := ProcessJobs(ctx, jobs, 5, 10)

	fmt.Println("error:", err)
	fmt.Println("Resultats:", len(Resultats))
}
