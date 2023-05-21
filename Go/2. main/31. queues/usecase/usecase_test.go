package usecase

import (
	"context"
	"errors"
	"fmt"
	"net/http"
	"testing"

	"github.com/tmvrus/pqueue/job"
	"github.com/tmvrus/pqueue/model"
	"github.com/tmvrus/pqueue/pqueue"
)

const defaultPriority uint8 = 1

func producerWorker(q pqueue.Queue) {
	req, _ := http.NewRequest(http.MethodGet, "http://localhost:8080", nil)
	j := job.NewCallbackRequest(req, http.DefaultClient)
	q.Push(j, defaultPriority)

}

func consumerWorker(q pqueue.Queue) {
	ctx := context.Background()
	for {
		j := q.Pull()
		if j == nil {
			fmt.Println("Finish.")
			return
		}

		if err := j.Execute(ctx); err != nil {
			if errors.Is(err, model.ErrRepeatable) {
				q.Push(j, defaultPriority)
			} else {
				fmt.Println("got non-repeatable error: " + err.Error())
			}
		}
	}
}

func Test_UseCase(t *testing.T) {
	q := pqueue.NewPQueue()
	producerWorker(q)
	consumerWorker(q)
}
