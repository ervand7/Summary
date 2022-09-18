package main

import (
	"fmt"
	"runtime"
	"time"
)

/*
Каналами можно заменить комбинацию из sync.Mutex и sync.Cond.
Для тренировки возьмите пример с sync.Cond из прошлого урока и переделайте
реализацию типа Queue так, чтобы она была основана на каналах.
*/

type Size struct {
	Width  uint32
	Height uint32
}

type Task struct {
	Filename string
	ToSize   Size
}

type Queue struct {
	ch chan *Task
}

func NewQueue() *Queue {
	return &Queue{
		ch: make(chan *Task, 1),
	}
}

func (q *Queue) Push(t *Task) {
	// получаем таску
	q.ch <- t
}

func (q *Queue) PopWait() *Task {
	return <-q.ch
}

type Resizer struct {
}

func NewResizer() *Resizer {
	r := Resizer{}
	return &r
}

func (r *Resizer) Resize(filename string, toSize Size) error {
	// пропустим реализацию
	time.Sleep(50 * time.Millisecond)
	return nil
}

type Worker struct {
	id      int
	queue   *Queue
	resizer *Resizer
}

func NewWorker(id int, queue *Queue, resizer *Resizer) *Worker {
	w := Worker{
		id:      id,
		queue:   queue,
		resizer: resizer,
	}
	return &w
}

func (w *Worker) Loop() {
	for {
		// записываем в переменную t таску, которую возьмем из канала
		t := w.queue.PopWait()

		err := w.resizer.Resize(t.Filename, t.ToSize)
		if err != nil {
			fmt.Printf("error: %v\n", err)
			continue
		}

		fmt.Printf("worker #%d resized %s\n", w.id, t.Filename)
	}
}

func main() {
	queue := NewQueue()
	workers := make([]*Worker, 0, runtime.NumCPU())

	// создаем 8 воркеров с одинаковой очередью
	for i := 0; i < runtime.NumCPU(); i++ {
		workers = append(workers, NewWorker(i, queue, NewResizer()))
	}

	for _, w := range workers {
		// У нас в программе есть всего один единственный канал queue.ch.
		// Здесь горутина, в которой мы вычитываем таску из канала,
		// заблокируется до тех пор, пока
		go w.Loop()
	}

	filenames := []string{"gopher.jpg", "test.png", "nonce.jpg"}
	for _, f := range filenames {
		// пока вот тут в канал не будет направлена новая таска
		queue.Push(
			// на лету создаем новую таску
			&Task{
				Filename: f, ToSize: Size{
					Width: 1024, Height: 1024,
				},
			})
	}

	time.Sleep(1 * time.Second)
}
