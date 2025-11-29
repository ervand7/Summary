package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var wg sync.WaitGroup

	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered in main:", r)
		}
	}()

	jobs := []int{1, 2, 3, 4, 5}

	for _, job := range jobs {
		wg.Add(1)
		go worker(job, &wg)
	}

	wg.Wait()
	fmt.Println("All workers finished")
	time.Sleep(300 * time.Millisecond)
}

func worker(id int, wg *sync.WaitGroup) {
	defer wg.Done()

	defer func() {
		if r := recover(); r != nil {
			fmt.Printf("Recovered in worker %d: %v\n", id, r)
		}
	}()

	if id%2 == 0 {
		panic(fmt.Sprintf("worker %d failed", id))
	}

	fmt.Println("Worker", id, "done")
}
