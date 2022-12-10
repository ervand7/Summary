package main

import (
	"fmt"
	"time"
)

// StopWatch - секундомер
type StopWatch struct {
	startOfProgram time.Time
	results        []time.Duration
}

/*
Start() — запустить/сбросить секундомер;
SaveSplit() — сохранить промежуточное время;
GetResults() []time.Duration — вернуть текущие результаты.
*/

func (s *StopWatch) Start() {
	s.startOfProgram = time.Now()
}

func (s *StopWatch) SaveSplit() {
	result := time.Now().Sub(s.startOfProgram)
	s.results = append(s.results, result)
}

func (s StopWatch) GetResults() []time.Duration {
	return s.results
}

func main() {
	sw := StopWatch{}
	// или
	// sw := new(StopWatch)
	sw.Start()

	time.Sleep(1 * time.Second)
	sw.SaveSplit()

	time.Sleep(500 * time.Millisecond)
	sw.SaveSplit()

	time.Sleep(300 * time.Millisecond)
	sw.SaveSplit()

	fmt.Println(sw.GetResults())
}

// [1.004643466s 1.505609247s 1.806269902s]
