package robot

import "fmt"

type Robot struct {
	model       string
	serialId    int
	workCounter int
}

func (r Robot) String() string {
	return fmt.Sprintf("Robot %s serialID %d", r.model, r.serialId)
}

// Work — робот выполняет работы и запоминает количество выполненных задач.
// Поэтому получатель метода — по указателю
func (r *Robot) Work(tasks []string) string {
	res := fmt.Sprintf("%s work:", r)
	for _, task := range tasks {
		res += "\n I do " + task
	}
	r.workCounter += len(tasks)
	return res
}
