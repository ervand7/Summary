package main

import (
	"fmt"
	"sync"
)

/*
Шаблон Посредник помогает уменьшить сцепление объектов в сложной системе
путём инкапсуляции связей между ними в одном объекте-посреднике. Отдельным
типам объектов для взаимодействия не нужно знать структуру и методы друг друга,
достаточно только знать интерфейс mediator. Благодаря этому код проще понимать,
поддерживать и модернизировать, особенно в сложных системах.
*/

// train — интерфейс поезда.
type train interface {
	requestArrival()
	departure()
	permitArrival()
}

// passengerTrain — конкретная реализация пассажирского поезда.
type passengerTrain struct {
	// ссылка на диспетчера
	mediator mediator
}

func (p *passengerTrain) requestArrival() {
	if p.mediator.canArrive(p) {
		fmt.Println("PassengerTrain: Arriving")
	} else {
		fmt.Println("PassengerTrain: Waiting")
	}
}

func (p *passengerTrain) departure() {
	fmt.Println("PassengerTrain: Leaving")
	p.mediator.notifyFree()
}

func (p *passengerTrain) permitArrival() {
	fmt.Println("PassengerTrain: Arrival Permitted. Arriving")
}

// goodsTrain — товарный поезд.
type goodsTrain struct {
	mediator mediator
}

func (g *goodsTrain) requestArrival() {
	if g.mediator.canArrive(g) {
		fmt.Println("GoodsTrain: Arriving")
	} else {
		fmt.Println("GoodsTrain: Waiting")
	}
}

func (g *goodsTrain) departure() {
	g.mediator.notifyFree()
	fmt.Println("GoodsTrain: Leaving")
}

func (g *goodsTrain) permitArrival() {
	fmt.Println("GoodsTrain: Arrival Permitted. Arriving")
}

// mediator — интерфейс диспетчера.
type mediator interface {
	canArrive(train) bool
	notifyFree()
}

// stationManager — реализация диспетчера.
type stationManager struct {
	isPlatformFree bool
	lock           *sync.Mutex
	trainQueue     []train
}

func newStationManger() *stationManager {
	return &stationManager{
		isPlatformFree: true,
		lock:           &sync.Mutex{},
	}
}

// canArrive сообщает, что платформа свободна, или ставит в очередь.
func (s *stationManager) canArrive(t train) bool {
	s.lock.Lock()
	defer s.lock.Unlock()
	if s.isPlatformFree {
		s.isPlatformFree = false
		return true
	}
	s.trainQueue = append(s.trainQueue, t)
	return false
}

func (s *stationManager) notifyFree() {
	s.lock.Lock()
	defer s.lock.Unlock()
	if len(s.trainQueue) > 0 {
		firstTrainInQueue := s.trainQueue[0]
		s.trainQueue = s.trainQueue[1:]
		firstTrainInQueue.permitArrival()
	} else if !s.isPlatformFree {
		s.isPlatformFree = true
	}
}

func main() {
	stationManager := newStationManger()
	passengerTrain := &passengerTrain{
		mediator: stationManager,
	}
	goodsTrain := &goodsTrain{
		mediator: stationManager,
	}
	passengerTrain.requestArrival()
	goodsTrain.requestArrival()
	passengerTrain.departure()
}

/*
PassengerTrain: Arriving
GoodsTrain: Waiting
PassengerTrain: Leaving
GoodsTrain: Arrival Permitted. Arriving
*/
