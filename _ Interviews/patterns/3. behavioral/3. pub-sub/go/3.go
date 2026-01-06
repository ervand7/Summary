package main

import "fmt"

/*
Паттерн pub-sub позволяет реализовать механизм подписки на события.
При этом издатели и подписчики не зависят друг от друга.
Подписчиков можно оповещать о событии в случайном порядке.
Абстрактный пример, в котором источник для оповещения вызывает метод
подписчика, может выглядеть так:
*/

// интерфейсы
type (
	publisher interface {
		register(observer)
		deregister(observer)
		notify()
	}
	observer interface {
		update(string)
		getID() string
	}
)

// реализация publisher
type event struct {
	observers   map[string]observer
	description string
}

func (e *event) register(o observer) {
	if e.observers == nil {
		e.observers = make(map[string]observer)
	}
	e.observers[o.getID()] = o
}

func (e *event) deregister(o observer) {
	delete(e.observers, o.getID())
}

func (e *event) notify() {
	for _, observer := range e.observers {
		observer.update(e.description)
	}
}

func (e *event) update(desc string) {
	e.description = desc
	e.notify()
}

// реализация observer
type subscribr struct {
	id string
}

func (s *subscribr) update(desc string) {
	fmt.Printf("The %s subscribr is notified of the %s event\n", s.id, desc)
}

func (s *subscribr) getID() string {
	return s.id
}

func main() {
	pub := new(event)
	sub1 := subscribr{"first"}
	sub2 := subscribr{"second"}
	sub3 := subscribr{"third"}
	pub.register(&sub1)
	pub.register(&sub2)
	pub.register(&sub3)
	pub.update("Alert")
}

/*
The first subscribr is notified of the Alert event
The second subscribr is notified of the Alert event
The third subscribr is notified of the Alert event
*/
