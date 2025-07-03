package main

import (
	"fmt"
	"sync"
	"time"
)

func worker(id int, jobs <-chan int, wg *sync.WaitGroup) {
	defer wg.Done()
	for job := range jobs {
		fmt.Printf("Worker %d processing job %d\n", id, job)
		time.Sleep(time.Second) // симуляция работы
	}
}

func main() {
	const numWorkers = 3
	const numJobs = 10

	jobs := make(chan int)
	var wg sync.WaitGroup

	// Запускаем воркеров
	for i := 1; i <= numWorkers; i++ {
		wg.Add(1)
		go worker(i, jobs, &wg)
	}

	// Отправляем задачи
	for j := 1; j <= numJobs; j++ {
		jobs <- j
	}
	close(jobs) // важно закрыть, чтобы воркеры завершились

	wg.Wait()
}
