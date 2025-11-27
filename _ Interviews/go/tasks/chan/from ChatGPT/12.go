package main

import (
	"fmt"
	"sync"
	"time"
)

// Goal:
// Run up to maxConcurrent tasks at once.
// Any additional tasks must wait.
// Question:
// Implement runTasks().

func main() {
	tasks := make([]func() int, 0)

	for i := 1; i <= 20; i++ {
		n := i
		tasks = append(tasks, func() int {
			time.Sleep(50 * time.Millisecond)
			return n * 2
		})
	}

	results := runTasks(tasks, 5)
	fmt.Println("result count:", len(results))
}

func runTasks(tasks []func() int, maxConcurrent int) []int {
	semaphore := make(chan struct{}, maxConcurrent)
	results := make([]int, len(tasks))

	var wg sync.WaitGroup

	for i, task := range tasks {
		wg.Add(1)

		semaphore <- struct{}{}

		go func(i int, t func() int) {
			defer wg.Done()
			defer func() { <-semaphore }()

			result := t()
			results[i] = result
		}(i, task)
	}

	wg.Wait()
	return results
}
