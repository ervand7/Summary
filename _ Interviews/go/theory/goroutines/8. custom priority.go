package main

// No Priority
// All goroutines are equal. The scheduler doesn't support priority levels. If you
// need prioritization:

type Task struct{}

func process(Task) {}

func main() {
	// Use separate channels with different polling rates
	highPriority := make(chan Task, 100)
	lowPriority := make(chan Task, 100)

	go func() {
		for {
			select {
			case task := <-highPriority:
				process(task)
			default:
				select {
				case task := <-highPriority:
					process(task)
				case task := <-lowPriority:
					process(task)
				}
			}
		}
	}()
}
