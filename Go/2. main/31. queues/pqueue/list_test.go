package pqueue

import (
	"context"
	"fmt"
	"testing"
)

type output struct {
	p uint8
}

func (i output) Execute(ctx context.Context) error {
	fmt.Println(i.p)
	return nil
}

func Test_List(t *testing.T) {
	q := NewPQueue()
	data := []uint8{1, 5, 6, 5, 2, 1, 12}
	for _, p := range data {
		q.Push(output{p}, p)
	}

	for {
		j := q.Pull()
		if j == nil {
			return
		}

		_ = j.Execute(context.Background())
	}
}

func printListNode(n *node) {
	if n.prev == nil {
		fmt.Print("nil,")
	} else {
		fmt.Print(n.prev.job)
	}
	if n == nil {
		fmt.Print("nil,")
	} else {
		fmt.Print(n.job)
	}
	if n.next == nil {
		fmt.Print("nil,")
	} else {
		fmt.Print(n.next.job)
	}
	fmt.Println()
}
